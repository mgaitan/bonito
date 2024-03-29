Bonito
------

Bonito is a very simple tool to generate numerated tickets (for instance, for solidarity events)
ready to be printed, clipped and cut, starting from a SVG template. 

The idea is to make "books" of consecutive tickets, in this way:

.. image:: http://mgaitan.github.io/images/bonito-8305a.png


It requires Inkscape and Ghostscript. 


How to use it
+++++++++++++++

Design your tickets as SVG marking the placeholder for the number 
as ``XXX`` [#]_. See this `design <https://github.com/mgaitan/bonito/blob/master/examples/mayores.svg>`_) as an example. 


Then run passing the number of consecutive tickets to clip together and the number of documents 
to generate. For example::

	
	bonito mayores.svg --group_by=5 --documents=2

This produces 2 documents, `mayores-001-015.pdf <https://github.com/mgaitan/bonito/blob/master/examples/mayores-001-015.pdf>`_  
and `mayores-016-030.pdf <https://github.com/mgaitan/bonito/blob/master/examples/mayores-016-030.pdf>`_ . 


See the `original blog post from 2010 <http://mgaitan.github.io/posts/bonito-feito-pero-efectivo/>`_ (in spanish) for further details. 



.. [#] You could use as many Xs as digit you want in the mark, and pass ``--mark`` in the command line.
	   For example, to print numbers from 0001, you could use ``XXXX`` as the mark and  
	   pass `--mark=XXXX`

