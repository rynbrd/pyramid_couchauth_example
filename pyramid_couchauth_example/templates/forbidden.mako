<%inherit file="/base.mako" />

<%def name="title()">Access Denied</%def>

<%def name="body()">
	<h1>Access Denied</h1>
	% if username == "":
	<p>Click <a href="/auth/login">here</a> to log in.</p>
	% else:
	<p>You do not have permission to view this page.</p>
	% endif
</%def>
