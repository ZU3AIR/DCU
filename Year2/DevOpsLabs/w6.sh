1. done
2. done
3.

made a directory
vim java-2.mk and add the github code
vim Add.java and add the code given
vim Subtract.java and add the code for add java into Subtract&replace add with Subtract
and change i+=1 to i-= 1 and save
make -f java-2.mk
einstein




4.  
dst = $(HOME)/local/bin
src = $(wildcard [a-z]*)

install: $(dst) $(addprefix $(dst)/, $(src))
		@true

$(dst)/%: %
		install -v -m 0555 $< $@

$(dst):
		mkdir -vp $@

.PHONY: install

5.
Copy and paste from github and paste to einstein

6.
