Prepare the variants/gene annotation data for the Miracum Galaxy workflows
==========================================================================

The following instructions can be followed from a Galaxy admin or a regular
user account. The user performing this, however, will be responsible for
providing the annotation data used by all runs of the Miracum analysis
workflows.

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
     https://usegalaxy.eu/datasets/11ac94870d0bb33abea3eb2f1b40fc3e/display?to_ext=data&hdca_id=82ce81c611294d8a&element_identifier=dbSNP.tidy
     https://usegalaxy.eu/datasets/11ac94870d0bb33a8142984ef06e3531/display?to_ext=data&hdca_id=82ce81c611294d8a&element_identifier=hotspots.data
     https://usegalaxy.eu/datasets/11ac94870d0bb33aa5105b08eaee1108/display?to_ext=data&hdca_id=82ce81c611294d8a&element_identifier=civic.variants
     https://usegalaxy.eu/datasets/11ac94870d0bb33a74e69e0263b752a0/display?to_ext=data&hdca_id=82ce81c611294d8a&element_identifier=cgi.variants
     https://usegalaxy.eu/datasets/11ac94870d0bb33aedeb453f1db5d19f/display?to_ext=data&hdca_id=82ce81c611294d8a&element_identifier=uniprot_cancer.genes
     https://usegalaxy.eu/datasets/11ac94870d0bb33ab24d9f463c0002b6/display?to_ext=data&hdca_id=82ce81c611294d8a&element_identifier=civic.genes
     https://usegalaxy.eu/datasets/11ac94870d0bb33a0e35b8cf7187e7ac/display?to_ext=data&hdca_id=82ce81c611294d8a&element_identifier=cgi.genes
     https://usegalaxy.eu/datasets/11ac94870d0bb33aa1c2191af7a79b9c/display?to_ext=data&hdca_id=82ce81c611294d8a&element_identifier=annotation.metadata
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

   **While you're waiting you can already continue with installing a helper
   workflow** that you will use to restructure the downloaded annotation data
   into the format expected by the analytical workflows.

   - Select ``Workflow`` from the top menu of your Galaxy

   - Find the ``Import`` button at the top-right of the page

   - Under ``Archived Workflow URL`` enter the URL:
     ``https://github.com/AG-Boerries/MIRACUM-Pipe-Galaxy/raw/master/workflows/Galaxy-Workflow-MIRACUM_prepare_annotation_data.ga``

   - Click ``Import workflow``

   Once the annotation data upload is complete you can run the helper workflow.

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

3. Make the annotation data available to all users

   - Select ``History options`` (the gearwheel icon at the top of the history
     panel), then ``Share or Publish`` under ``History Actions``
     
     This will take you to the ``Share or Publish History`` page of your Galaxy.

   - You want to select ``Make History Accessible and Publish``, but **before**
     you do, you need to click the
     ``Also make all objects within the History accessible.`` checkbox (or
     other users would be able to see the history, but would not be able to use
     any of its datasets).

   The helper workflow for structuring the annotation data is *not* required
   for your users so you do not need to share it.

**Congratulations!**
The Miracum annotation data should now be accessible to every registered user
on your Galaxy server.
