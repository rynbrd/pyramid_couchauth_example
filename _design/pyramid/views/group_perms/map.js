function(doc) {
	if (doc.doc_type == 'Group') {
		for (var i in doc.permissions) {
			emit(doc.name, doc.permissions[i].name);
		}
	}
}
