+++
date = "2024-11-21"
title = "MVP on AWS: PostgreSQL"
slug = "aws-mvp-postgresql"
tags = [
    "aws",
    "rds",
    "postgresql",
]
categories = [
    "aws",
]
series = ["AWS"]
+++

## Why PostgreSQL?
Let's assume that you already decided on PostgreSQL as your database. Why? Because it is a powerful, open-source object-relational database system with over 30 years of active development, correct?  We will leave the problem of where and how to store data for another time.

## RDS Aurora (PostgreSQL Compatible) or RDS PostgreSQL
If there are no specific requirements, we may select Aurora as the default option. 
Storage systems are the key difference between the two. You don't have to worry about being out of space. Aurora will help you. Aurora will automatically scale the storage up to 128 TB (November 2024). "The data is automatically replicated across Availability Zones, your data is highly durable with less possibility of data loss." You can have one instance with data in 3 different places. If you want to add another region, it will give us six different places in the world where data is stored. Magic, right? 

## PostgreSQL parameters
There are many parameters that could be changed. But let's focus on the most important and popular.
Please create two custom parameter groups for cluster and, for instance, in advance and don't use the default ones. We are unable to modify the defaults, and some parameters require a cluster/instance reboot.

- `log_min_duration_statement = 4000` - The duration of the statement in milliseconds beyond which statements will be logged. 0 logs all statements. The default is -1, logging is disabled. [More info](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-MIN-DURATION-STATEMENT)
- `rds.force_ssl = 1` - Forces the use of SSL for all connections. The default is 0 (off). Force the encryption in transit. [More info](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.SSL.html)
- `log_lock_waits = 1` - Logs long lock waits. The default is off. [More info](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-LOCK-WAITS)
- `max_locks_per_transaction` - Sets the maximum number of locks per transaction. The default is 64. [More info](https://www.postgresql.org/docs/current/runtime-config-locks.html#GUC-MAX-LOCKS-PER-TRANSACTION)
- `shared_preload_libraries = pg_stat_statements,pgaudit` - Specifies one or more shared libraries to preload into server memory. The default is an empty string. More info: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.html
- `idle_in_transaction_session_timeout = 300000` - Terminate any session with an open transaction that has been idle for longer than the specified duration in milliseconds. The default is 0 (off). [More info](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-IDLE-IN-TRANSACTION-SESSION-TIMEOUT)
- `log_autovacuum_min_duration = 60000` - Sets the minimum execution time above which autovacuum actions will be logged. The default is -1, logging is disabled. [More info](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-AUTOVACUUM-MIN-DURATION)


## Creation from the console process
Let's assume that our urgent needs and luck of time and knowledge force us to use the console. What better to select, where to click? 

1. Choose the production template always. Fix the DB cluster identifier, it will be used in the connection string. Use any root username. Follow the defaults for AWS Secrets Manager Integration. It will add automatic root password rotation.

![Image](/images/posts/aws_mvp_postresql/1.webp)

2. Size and Storage. Use Aurora Standard and any T class to optimize the budget a bit. You could change it later.

![Image](/images/posts/aws_mvp_postresql/2.webp)

3. Serverless v2. If you use it very rarely and have no idea about the load, you could use the serverless v2. It will scale automatically. From 0 to the sky. Much more expensive, but very flexible.

![Image](/images/posts/aws_mvp_postresql/3.webp)

4. Connectivity. ATTENTION! Do not use the default VPC here. It takes around 5-10 minutes to clickops a separate VPC. And after database creation, you can't change its VPC. Significant moment. Moving a production database could cost you many hours. The same for public access. Avoid it. Use VPNs, Direct Connect, Balancers, and RDS Proxy. It takes time to understand what is consuming the database from the outside. 

![Image](/images/posts/aws_mvp_postresql/4.webp)

5. Connectivity again. Don't use the default security group (firewall). Just create a new one. Even if the rules will be bad and wrong, it is better to have a separate entity that will be used only for this database.

![Image](/images/posts/aws_mvp_postresql/5.webp)

6. Database parameters. Choose the custom parameter groups that were created above. Not default. It is possible to change, but requires an instance/cluster reboot. 

7. Encryption at rest. Always create a separate multi-region KMS key. At least one Customer Managed KMS key could help a lot. We can't change encryption parameters after the database creation. The same applies to the performance insights.

![Image](/images/posts/aws_mvp_postresql/7.webp)

## Creation from Terrafom
The same thing as above, but as code.
There is no need to repeat that again. This code is already available.
https://github.com/terraform-aws-modules/terraform-aws-rds-aurora/blob/master/examples/postgresql/main.tf 

```hcl
provider "aws" {
  region = local.region
}

data "aws_availability_zones" "available" {}

locals {
  name   = "ex-${basename(path.cwd)}"
  region = "eu-west-1"

  vpc_cidr = "10.0.0.0/16"
  azs      = slice(data.aws_availability_zones.available.names, 0, 3)

  tags = {
    Example    = local.name
  }
}

################################################################################
# RDS Aurora Module
################################################################################

module "aurora" {
  source  = "terraform-aws-modules/rds-aurora/aws"
  version = "~> 9.0"

  name            = local.name
  engine          = "aurora-postgresql"
  engine_version  = "16.3"
  master_username = "pgroot"
  storage_encrypted = true
  kms_key_id        = module.kms.key_id
  instances = {
    1 = {
      instance_class          = "db.t4.medium"
    }
  }
  vpc_id               = module.vpc.vpc_id
  db_subnet_group_name = module.vpc.database_subnet_group_name
  security_group_rules = {
    vpc_ingress = {
      cidr_blocks = module.vpc.private_subnets_cidr_blocks
    }
  }

  apply_immediately   = true

  engine_lifecycle_support = "open-source-rds-extended-support-disabled"

  create_db_cluster_parameter_group      = true
  db_cluster_parameter_group_name        = local.name
  db_cluster_parameter_group_family      = "aurora-postgresql16"
  db_cluster_parameter_group_description = "${local.name} example cluster parameter group"
  db_cluster_parameter_group_parameters = [
    {
      name         = "log_min_duration_statement"
      value        = 4000
      apply_method = "immediate"
      }, {
      name         = "rds.force_ssl"
      value        = 1
      apply_method = "immediate"
      }, {
      name         = "log_lock_waits"
      value        = "1"
      apply_method = "immediate"
      }, {
      name         = "max_locks_per_transaction"
      value        = "1000"
      apply_method = "pending-reboot"
      }, {
      name         = "shared_preload_libraries"
      value        = "pg_stat_statements,pgaudit"
      apply_method = "pending-reboot"
      }, {  
      name         = "idle_in_transaction_session_timeout"
      value        = "300000" # Max 5 minutes per transaction
      apply_method = "immediate"
      }, {
      name         = "log_autovacuum_min_duration"
      value        = "60000" # 1m, minimum execution time above which autovacuum actions will be logged
      apply_method = "immediate"
    }
  ]

  create_db_parameter_group      = true
  db_parameter_group_name        = local.name
  db_parameter_group_family      = "aurora-postgresql16"
  db_parameter_group_description = "${local.name} example DB parameter group"
  db_parameter_group_parameters = [
    {
      name         = "log_min_duration_statement"
      value        = 4000
      apply_method = "immediate"
    }
  ]

  enabled_cloudwatch_logs_exports = ["postgresql"]
  create_cloudwatch_log_group     = true

  cloudwatch_log_group_tags = {
    Sensitivity = "high"
  }

  tags = local.tags
}

################################################################################
# Supporting Resources
################################################################################

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"

  name = local.name
  cidr = local.vpc_cidr

  azs              = local.azs
  public_subnets   = [for k, v in local.azs : cidrsubnet(local.vpc_cidr, 8, k)]
  private_subnets  = [for k, v in local.azs : cidrsubnet(local.vpc_cidr, 8, k + 3)]
  database_subnets = [for k, v in local.azs : cidrsubnet(local.vpc_cidr, 8, k + 6)]

  tags = local.tags
}

module "kms" {
  source  = "terraform-aws-modules/kms/aws"
  version = "~> 2.0"

  deletion_window_in_days = 7
  description             = "KMS key for ${local.name} cluster activity stream."
  enable_key_rotation     = true
  is_enabled              = true
  key_usage               = "ENCRYPT_DECRYPT"

  aliases = [local.name]

  tags = local.tags
}

```

## What's next? Other options? 
Today we covered the PostgreSQL on RDS Aurora. But there are many other options. 
The cheapest is to store the raw data as S3 objects. Durable and replication is available, but it could be slow. 
Key-value stores like DynamoDB. It is fast, but it is not a relational database. 
The most important thing is to start with the problem and then pick the right tool for it.

