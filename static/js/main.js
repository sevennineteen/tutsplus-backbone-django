(function () {
	window.App = {
		Models: {},
		Collections: {},
		Views: {},
		Router: {}
	};

	window.vent = _.clone(Backbone.Events);

	window.template = function (id) {
		return _.template($('#' + id).html());
	};
})();