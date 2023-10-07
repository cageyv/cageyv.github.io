## Portfolio Landing Page
https://cageyv.github.io/

## Notes
- Image optimization via imagemagick: `mogrify -path output -quality 90 -strip -define jpeg:extent=200KB *.jpeg`
- Image conversion: `find ./ -type f -name '*.png' -exec sh -c 'cwebp -q 85 $1 -o "${1%.png}.webp"' _ {} \;`