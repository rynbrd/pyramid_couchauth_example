function(doc) {
	if (doc.doc_type == 'Group') {
		for (var i in doc.permissions) {
			emit(doc.permissions[i].name, doc.name);
		}
	}
}
