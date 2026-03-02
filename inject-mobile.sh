#!/bin/zsh
find . -name "*.html" -not -path "*/.git/*" | while read file; do
  echo "-> $file"
  if ! grep -q "mobile.css" "$file"; then
    sed -i.bak 's|</head>|  <link rel="stylesheet" href="/mobile.css">\n</head>|' "$file"
    echo "   ok mobile.css"
  fi
  if ! grep -q "mobile-nav.js" "$file"; then
    sed -i.bak 's|</body>|  <script src="/mobile-nav.js"></script>\n</body>|' "$file"
    echo "   ok mobile-nav.js"
  fi
  rm -f "${file}.bak"
done
echo "FATTO"
