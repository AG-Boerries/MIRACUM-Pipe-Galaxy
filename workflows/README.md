Adding the Miracum workflows to your server
===========================================

The following instructions can be followed from a Galaxy admin or a regular
user account. The user performing this, however, will be responsible for
providing the workflows governing all future analysis runs on the server.

To import the latest versions of all workflows intended for regular users,

1. Go to *Workflows* in the top menu of the Galaxy web interface
2. Click the *Import button* at the top-right of the central part of the screen.
3. Under *Archived Workflow URL* provide the link to the first workflow of
   this repository:
   
   ```
   https://github.com/AG-Boerries/MIRACUM-Pipe-Galaxy/raw/master/workflows/Galaxy-Workflow-MIRACUM_WES_complete.ga
   ```
   
4. Repeat steps 2 and 3 with the following additional URLs:

   ```
   https://github.com/AG-Boerries/MIRACUM-Pipe-Galaxy/raw/master/workflows/Galaxy-Workflow-MIRACUM_panel_complete.ga
   https://github.com/AG-Boerries/MIRACUM-Pipe-Galaxy/raw/master/workflows/Galaxy-Workflow-MIRACUM_merge-per_lane_fastq_data.ga
   ```
   
5. Publish all imported workflows on the Galaxy server to make them accessible
   to all users:
   
   1. Click the "arrow-down" icon next to each workflow's name to expand its
      select menu and choose ``Share``
   2. On the workflow sharing page, select
      ``Make Workflow Accessible and Publish``

Registered users can now find these workflows by selecting
``Shared Data`` -> ``Workflows`` from Galaxy's top menu. This brings up a
complete list of published workflows on your server, from which users can
directly run any workflow by selecting the "arrow-down" expanding menu next to
the workflow's name.

Please note that directly running the shared workflows is strongly preferable
over importing them first into a user's personal workflow list. Importing
would create a user-specific *copy* of the workflow, which would get
out-of-sync with the latest available version over time as workflow updates
become available.

=> **Running shared workflows directly from the ``Published Workflows`` list
ensures that all users are always using the latest version of any workflow.**

