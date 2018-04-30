/**
*
* @license Guriddo jqGrid JS - v5.3.0 
* Copyright(c) 2008, Tony Tomov, tony@trirand.com
* 
* License: http://guriddo.net/?page_id=103334
*/
!function(a){"use strict";"function"==typeof define&&define.amd?define(["jquery"],a):a(jQuery)}(function(a){"use strict";var b,c=a();a.fn.html5sortable=function(d){var e=String(d);return d=a.extend({connectWith:!1},d),this.each(function(){var f;if(/^enable|disable|destroy$/.test(e))return f=a(this).children(a(this).data("items")).attr("draggable","enable"===e),void("destroy"===e&&f.add(this).removeData("connectWith items").off("dragstart.h5s dragend.h5s selectstart.h5s dragover.h5s dragenter.h5s drop.h5s"));var g,h;f=a(this).children(d.items);var i=a("<"+(/^ul|ol$/i.test(this.tagName)?"li":/^tbody$/i.test(this.tagName)?"tr":"div")+' class="sortable-placeholder '+d.placeholderClass+'">').html("&nbsp;");f.find(d.handle).mousedown(function(){g=!0}).mouseup(function(){g=!1}),a(this).data("items",d.items),c=c.add(i),d.connectWith&&a(d.connectWith).add(this).data("connectWith",d.connectWith),f.attr("draggable","true").on("dragstart.h5s",function(c){if(d.handle&&!g)return!1;g=!1;var e=c.originalEvent.dataTransfer;e.effectAllowed="move",e.setData("Text","dummy"),h=(b=a(this)).addClass("sortable-dragging").index()}).on("dragend.h5s",function(){b&&(b.removeClass("sortable-dragging").show(),c.detach(),h!==b.index()&&b.parent().trigger("sortupdate",{item:b,startindex:h,endindex:b.index()}),b=null)}).not("a[href], img").on("selectstart.h5s",function(){return this.dragDrop&&this.dragDrop(),!1}).end().add([this,i]).on("dragover.h5s dragenter.h5s drop.h5s",function(e){return!f.is(b)&&d.connectWith!==a(b).parent().data("connectWith")||("drop"===e.type?(e.stopPropagation(),c.filter(":visible").after(b),b.trigger("dragend.h5s"),!1):(e.preventDefault(),e.originalEvent.dataTransfer.dropEffect="move",f.is(this)?(d.forcePlaceholderSize&&i.height(b.outerHeight()),b.hide(),a(this)[i.index()<a(this).index()?"after":"before"](i),c.not(i).detach()):c.is(this)||a(this).children(d.items).length||(c.detach(),a(this).append(i)),!1))})})}});