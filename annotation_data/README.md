Prepare the variants/gene annotation data for the Miracum Galaxy workflows
==========================================================================

1. Create a new empty history and give it a suitable name

   *Miracum annotation data* could be such a name.

2. Upload the current version of the annotation data

   - Open the Galaxy Upload Manager (by clicking the upload icon on the
     top-right of the tool panel)

   - In the ``Download from web or upload from disk`` dialogue window,
     select the ``Collection`` tab, then ``Paste/Fetch data``.

   - Copy the following links into the text box under
     ``Download data from the web by entering URLs (one per line) or directly paste content.``:

     ```
     https://usegalaxy.eu/datasets/11ac94870d0bb33af8a0b58436090b1f/display?to_ext=data&hdca_id=32acb0c597889ace&element_identifier=dbSNP.tidy
     https://usegalaxy.eu/datasets/11ac94870d0bb33aae6dafccda2f98ce/display?to_ext=data&hdca_id=32acb0c597889ace&element_identifier=hotspots.data
     https://usegalaxy.eu/datasets/11ac94870d0bb33a3db9ccac021aab7f/display?to_ext=data&hdca_id=32acb0c597889ace&element_identifier=civic.variants
     https://usegalaxy.eu/datasets/11ac94870d0bb33ab81bfc56727e2942/display?to_ext=data&hdca_id=32acb0c597889ace&element_identifier=cgi.variants
     https://usegalaxy.eu/datasets/11ac94870d0bb33a11fcc194ba0ac3c9/display?to_ext=data&hdca_id=32acb0c597889ace&element_identifier=uniprot_cancer.genes
     https://usegalaxy.eu/datasets/11ac94870d0bb33a075823877241b126/display?to_ext=data&hdca_id=32acb0c597889ace&element_identifier=civic.genes
     https://usegalaxy.eu/datasets/11ac94870d0bb33aaba0d2b1d7be95e2/display?to_ext=data&hdca_id=32acb0c597889ace&element_identifier=cgi.genes
     https://usegalaxy.eu/datasets/11ac94870d0bb33a239a2350da3ca8b2/display?to_ext=data&hdca_id=32acb0c597889ace&element_identifier=annotation.metadata
     ```

   - Click ``Start``

2. Arrange datasets into the format expected by the Miracum analysis workflows

   - While your datasets are getting uploaded, click the now available
     ``Build`` in the upload manager dialogue (if you have closed the dialogue
     window, simply reopen it by clicking on the Upload icon again).

   - In the ensuing ``Create a collection from a list of datasets`` dialogue
     provide a name for the new collection, e.g. *Uploaded data*, then click
     ``Create list``.

     All datasets should now be gathered into a single collection in your
     history.

   - Wait for the upload jobs to finish

     It can take approx. 30 minutes until all data is uploaded.

     You can check the status of the uploads by clicking on the newly created
     collection in your history, which will reveal its contained datasets.

     While an upload job is running the corresponding dataset will be shown in
     yellow. A dataset's color will change to green, when its upload is
     complete. If a dataset turns red instead, this indicates an error during
     the data upload.

     Please note, however, that the status of your uploads inside the
     collection will not be updated automatically. Instead you'll have to click
     the ``Refresh history`` icon at the top of the history panel (and then
     navigate back into the collection) to see the current status.

   - Select ``Workflow`` from the top menu of your Galaxy

   - Find the ``MIRACUM - Prepare annotation data`` workflow in the list of
     available workflows and click the ``Run Workflow`` icon (at the very right
     of the workflow record).

   - Select the collection you just built as the
     ``Downloaded annotation data as collection`` and click ``Run Workflow``.

     If the collection is not offered in the select menu, then either the
     uploads of its contained datasets are not complete yet, or there has been
     an error with at least one of the uploads.

     In the first case you just have to wait for the uploads to complete before
     trying to run the workflow. In the second case, the simplest solution is
     to discard the collection and start over.
     
