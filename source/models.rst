Models
======

Here is information that is relevant for users and new developers also developers
who may have forgotten somet things.

This information is available to see for all.

.. tab-set::

   .. tab-item:: Useful topic name for users
      :sync: key1

      Here is some information for users about somtihng
      in nest that is user specific

      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
      Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis
      aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
      Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

   .. tab-item:: The technical details
      :sync: key2

      But you can find different info here for developers about
      it

Some universal knowledge for everyone  to know aboiut


.. tab-set::

   .. tab-item:: Another useful topic name for users
      :sync: key1

      Here is some additional information information for users about somtihng
      in nest

      Lorem ipsum text

   .. tab-item:: More technical details
      :sync: key2

      But this is the info that developers need

      .. mermaid::

        sequenceDiagram
          user -> simulation_manager: prepare()
          simulation_manager -> node_manager: prepare_nodes()
          node_manager -> node: init()
          node_manager -> node: pre_run_hook()
          Note left of node_manager: state:<br/>prepared
          user -> simulation_manager: run()
          Note right of simulation_manager: 1
          user -> simulation_manager: run()
          Note left of user: store results<br/>...
          user -> simulation_manager: cleanup()

.. dropdown:: We could also have hidden info in dropdowns
   :animate: fade-in
   :color: secondary

   BOO!

   .. image:: _static/img/brain-only.svg
      :width: 50%
