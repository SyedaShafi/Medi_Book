function setDeleteFormAction(slug) {
  document.getElementById('deleteForm').action = `/delete/${slug}/`;
}
