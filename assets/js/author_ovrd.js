function type(words, element, index){
    index = index ? index : 0;
    (function writer(i){
      var string = words[index];
      if(string.length <= i++){
        element.innerText = string;
        if(words[index] != words[words.length-1]) {
            setTimeout(function() {
            reverseType(words, element, index);
          },500);
        }else{
          setTimeout(function() {
            reverseType(words,element, index);
          },2000);
        }
        return;
      }
      element.innerText = string.substring(0,i);
      var rand = Math.floor(Math.random() * (100)) + 40;
      setTimeout(function(){writer(i);},rand);
    })(0)
  }
  
  function reverseType(words, element, index){
    index = index ? index : 0;
    (function writer(i){
      var string = words[index];
      if(string.length <= i++){
        element.innerText = string;
        if(words[index] != words[words.length-1]) {
          type(words, element, index+1);
        }else{
          type(words, element, 0);           
        }
        return;
      }
      element.innerText = string.substring(0,string.length - i);
      var rand = Math.floor(Math.random() * (100)) + 10;
      setTimeout(function(){writer(i);},rand);
    })(0)
  }



