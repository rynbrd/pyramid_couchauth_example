<%inherit file="/base.mako" />

<%def name="title()">Welcome</%def>

<%def name="body()">
	<h1>Welcome</h1>
	<a href="/page/public">Public</a> -
	<a href="/page/private">Private</a> -
	<a href="/auth/logout">Log Out</a>
</%def>
