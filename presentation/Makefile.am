CLOCAL_AMFLAGS = -I config/m4 -I aclocal
clean:
	latexmk -c

dot:
	for myfile in $(shell ls *.dot |cut -f1 -d'.'|uniq); do dot -Tpng $$myfile.dot > ../images/$$myfile.png;done

presentation: 
	latexmk -pdf -synctex=1 -shell-escape gnn-pres

