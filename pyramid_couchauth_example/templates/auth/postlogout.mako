<%inherit file="/base.mako" />

<%def name="title()">Goodbye!</%def>

<%def name="body()">
	<h1>Goodbye!</h1>
	<a href="/page/public">Public</a> -
	<a href="/page/private">Private</a> -
	<a href="/auth/login">Log In Again</a>
</%def>

