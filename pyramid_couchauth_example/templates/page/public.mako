<%inherit file="/base.mako" />

<%def name="title()">Public Page</%def>

<%def name="body()">
	<h1>Public Page!</h1>
	<p>You're viewing an unprotected page!</p>
	<a href="/page/private">Private</a>
	% if username != "":
	- <a href="/auth/logout">Logout</a>
	% endif
</%def>

