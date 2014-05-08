WebStatus
=========

API and server query results, and eventually staff management of users.

Currently developed using Flask, to be deployed on MCME build server.

Development url is currently at mcme.joshr.hk


Current Endpoints
=================
All output json.

###Users Groups
e.g. mcme.joshr.hk/export/<group>
  *(use mcme ranks, non-plural: valar, foreman, artisan, etc.)*

###Individual Users
e.g. mcme.joshr.hk/export/user/<name>

###Servers
e.g. mcme.joshr.hk/server/build
  *(also /freebuild)*
