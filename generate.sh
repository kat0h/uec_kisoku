echo "# 電通大 規則" > index.md
ls md | grep -v "^_" | sed 's/\.md//' | xargs -I@ echo "- [@](./md/@)  " >> index.md
