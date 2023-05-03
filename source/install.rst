Install
=======

.. _admon:

Admonitions
-----------


.. note::

    Here is a note to describe important information for reader

.. seealso::

   Here provide links to relevant content

.. warning::

   Use this if there is a risk of problems 

.. admonition:: custom

   This is a custom admonition if you want to include a title


.. important:: Here is something important


.. code-block:: html

    <span style="font-size: 2rem;" class="md-icon">&#xe869;</span>

translates to a the site's icon:

.. raw:: html

    <span style="font-size: 2rem;" class="md-icon">&#xe869;</span>

The material icon font provides hundreds to choose from. You can use the ``<i>`` tag or the
``<span>`` tag.

.. raw:: html

    <i style="font-size: 1rem;" class="md-icon">&#xe158;</i>
    <i style="font-size: 1.2rem;" class="md-icon">&#xe155;</i>
    <i style="font-size: 1.4rem;" class="md-icon">&#xe195;</i>

Simple
------

A simple table:

=====  =====  =======
H1     H2     H3
=====  =====  =======
cell1  cell2  cell3
...    ...    ...
...    ...    ...
=====  =====  =======

List Tables
-----------

.. list-table:: A List Table
   :header-rows: 1

   * - Column 1
     - Column 2
   * - Item 1
     - Item 2
