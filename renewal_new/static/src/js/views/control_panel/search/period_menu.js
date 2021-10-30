odoo.define('renewal_new.PeriodMenu', function (require) {
"use strict";

var config = require('web.config');
var core = require('web.core');
var Domain = require('web.Domain');
var DropdownMenu = require('web.DropdownMenu');
var search_filters = require('web.search_filters');
var filter_menu = require('web.FilterMenu')
//console.log("filter_menu are: ", filter_menu)



var _t = core._t;
var QWeb = core.qweb;

var PeriodMenu = filter_menu.include({

        events: _.extend({}, filter_menu.prototype.events, {
            'click .o_add_custom_period': '_onAddCustomPeriodClick',
        }),

        init: function (parent, filters, fields) {
            this._super(parent, filters);

            // determines when the 'Add custom Period' submenu is open
            this.generatorPeriodMenuIsOpen = false;

        },


        _renderGeneratorPeriodMenu: function () {
            this.$el.find('.o_generator_menu').remove();
            if (!this.generatorPeriodMenuIsOpen) {
                _.invoke(this.propositions, 'destroy');
                this.propositions = [];
            }
            var $generatorMenu = QWeb.render('FilterMenuGenerator', {widget: this});
            this.$menu.append($generatorMenu);
            this.$addFilterMenu = this.$menu.find('.o_add_filter_menu');
            this.$dropdownReference.dropdown('update');
        },

        _toggleCustomPeriodMenu: function () {
            this.generatorPeriodMenuIsOpen = !this.generatorPeriodMenuIsOpen;
            this._renderGeneratorPeriodMenu();
        },

        _onAddCustomPeriodClick: function (ev) {
            ev.preventDefault();
            ev.stopPropagation();
            this._toggleCustomPeriodMenu();
        },
});

return PeriodMenu;

});
