.PHONY: all
all: out/outline.pdf

.PHONY: clean
clean:
	rm out/outline.md
	rm out/deps.svg
	rmdir out

out:
	mkdir out

out/deps.svg: ./outline.md ./extract_dot.py ./out
	./extract_dot.py ./outline.md | dot -Tsvg > "$@"

out/outline.html: ./outline.md ./header.html ./footer.html out ./out/deps.svg
	cat ./header.html > "$@"
	./extract_dot.py ./outline.md --invert | markdown >> "$@"
	cat ./footer.html >> "$@"

out/outline.pdf: ./out/outline.html
	wkhtmltopdf "$<" "$@"

metrics: example/metrics.cpp
	clang++ -std=c++17 '$<' -o '$@'
