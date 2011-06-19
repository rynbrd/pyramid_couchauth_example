<%inherit file="/base.mako" />

<%def name="title()">Private Page</%def>

<%def name="body()">
	<h1>Private Page!</h1>
	<p>You're viewing a protected page!</p>
	<a href="/page/public">Public</a> -
	<a href="/auth/logout">Logout</a>
</%def>

