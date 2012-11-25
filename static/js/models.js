App.Models.Contact = Backbone.Model.extend({
	// validate
	validate: function (attrs) {
		if (! attrs.first_name || ! attrs.last_name ) {
			return 'First and Last names required';
		}
		if (! attrs.email_address ) {
			return 'Email required';
		}
	}
});