all: linked-data-outline.html

linked-data-outline.html:
	emacs -batch --visit linked-data-outline.org --funcall org-export-as-html


clean:
	rm -f linked-data-outline.html
