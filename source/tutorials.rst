Tutorials
=========


PyNEST tutorial explain here is where you should start if you dont know nest


Test grid variants
-------------------

.. grid:: 1 2 2 2
   :outline:

   .. grid-item::

     .. grid:: 1 1 1 1

        .. grid-item::
            :columns: auto

            .. code-block:: python

                import nest

                neurons = nest.Create("iaf_psc_alpha", 10000, {
                    "V_m": nest.random.normal(-5.0),
                    "I_e": 1000.0
                })
                input = nest.Create("noise_generator", params={
                    "amplitude": 500.0
                })
                nest.Connect(input, neurons, syn_spec={'synapse_model': 'stdp_synapse'})
                spikes = nest.Create("spike_recorder", params={
                    'record_to': 'ascii',
                    'label': 'excitatory_spikes'
                })
                nest.Connect(neurons, spikes)
                nest.Simulate(100.0)
                nest.raster_plot.from_device(spikes, hist=True)
                plt.show()

   .. grid-item::

     .. grid:: 1 1 1 1


        .. grid-item-card:: API Docs
            :columns: auto

            * :py:func:`.Create`
            * :py:func:`.Connect`
            * :py:func:`.Simulate`
            * See all PyNEST functions

        .. grid-item-card:: Guides
            :columns: auto

            * :ref:`link_to_neurondocs`

            * :ref:`link_to_connectiondocs`

            * :ref:`link_to_docs`



