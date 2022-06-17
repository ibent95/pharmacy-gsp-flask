(self["webpackChunkpython_webpack_boilerplate"] = self["webpackChunkpython_webpack_boilerplate"] || []).push([["app"],{

/***/ "./frontend/src/components/sidebar.js":
/*!********************************************!*\
  !*** ./frontend/src/components/sidebar.js ***!
  \********************************************/
/***/ (() => {

window.console.log("sidebar is loaded");

/***/ }),

/***/ "./frontend/src/js/app.js":
/*!********************************!*\
  !*** ./frontend/src/js/app.js ***!
  \********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _scss_app_scss__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../scss/app.scss */ "./frontend/src/scss/app.scss");
/* harmony import */ var _components_sidebar__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../components/sidebar */ "./frontend/src/components/sidebar.js");
/* harmony import */ var _components_sidebar__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_components_sidebar__WEBPACK_IMPORTED_MODULE_1__);
// This is the scss entry file
 // We can import Bootstrap JS instead of the CDN link, if you do not use
// Bootstrap, please feel free to remove it.
//import "bootstrap/dist/js/bootstrap.bundle";
// We can import other JS file as we like


window.document.addEventListener("DOMContentLoaded", function () {
  window.console.log("dom ready 1");
});

/***/ }),

/***/ "./frontend/src/scss/app.scss":
/*!************************************!*\
  !*** ./frontend/src/scss/app.scss ***!
  \************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
// extracted by mini-css-extract-plugin


/***/ }),

/***/ "./frontend/src/ts/app.ts":
/*!********************************!*\
  !*** ./frontend/src/ts/app.ts ***!
  \********************************/
/***/ (() => {

"use strict";

//// const ID_RE: any = /(-)_(-)/;
//const ID_RE: any = /(-)_/;
///**
//* Replace the template index of an element (-_-) with the
//* given index.
//*/
//function replaceTemplateIndex(value: any, index: any) {
//	// value.replace(ID_RE, '$1' + index + '$2')
//	return value.replace(ID_RE, '$1' + index);
//}
///**
//* Adjust the indices of form fields when removing items.
//*/
//function adjustIndices(this: any, removedIndex: any) {
//	let forms: any = document.getElementsByClassName('productItem');
//	forms.each( (i: number) => {
//		// let form: any = $(this);
//		let form: any = document.querySelectorAll(this);
//		let index: any = parseInt(form.data('index'));
//		let newIndex: any = index - 1;
//		if (index < removedIndex) {
//			// Skip
//			return true;
//		}
//		// This will replace the original index with the new one
//		// only if it is found in the format -num-, preventing
//		// accidental replacing of fields that may have numbers
//		// intheir names.
//		// let regex: any = new RegExp('(-)'+index+'(-)');
//		// let repVal: any = '$1'+newIndex+'$2';
//		let regex: any = new RegExp('(-)' + index);
//		let repVal: any = '$1' + newIndex;
//		// Change ID in form itself
//		form.attr('id', form.attr('id').replace(index, newIndex));
//		form.data('index', newIndex);
//		// Change IDs in form fields
//		form.find('label, input, select, textarea').each( (j: any) => {
//			// let item: any = $(this);
//			let item: any = document.querySelectorAll(this);
//			if (item.is('label')) {
//				// Update labels
//				item.attr('for', item.attr('for').replace(regex, repVal));
//				return;
//			}
//			// Update other fields
//			item.attr('id', item.attr('id').replace(regex, repVal));
//			item.attr('name', item.attr('name').replace(regex, repVal));
//		});
//	});
//}
///**
//* Remove a form.
//*/
//function removeForm(productItemIndex: any) {
//	// let removedForm: any = $(this).closest('.subform');
//	let removedForm: any = document.getElementById('productItem-' + productItemIndex);
//	let removedIndex: any = parseInt(removedForm.data('index'));
//	removedForm.remove();
//	// Update indices
//	adjustIndices(removedIndex);
//}
///**
//* Add a new form.
//*/
//function addForm() {
//	let templateForm: any = document.getElementById('productItem-_');
//	if (templateForm.length == 0) {
//		console.log('[ERROR] Cannot find template');
//		return;
//	}
//	// Get Last index
//	document.querySelectorAll('productItem');
//	let lastForm: any = document.querySelectorAll('productItem')[document.querySelectorAll('productItem').length - 1];
//	let newIndex: any = 0;
//	if (lastForm.length > 0) {
//		newIndex = parseInt(lastForm.data('index')) + 1;
//	}
//	// Maximum of 20 subforms
//	if (newIndex >= 20) {
//		console.log('[WARNING] Reached maximum number of elements');
//		return;
//	}
//	// Add elements
//	let newForm: any = templateForm.clone();
//	newForm.attr('id', replaceTemplateIndex(newForm.attr('id'), newIndex));
//	newForm.data('index', newIndex);
//	newForm.find('label, input, select, textarea').each(function (this: any, idx: any) {
//		// let item: any = $(this);
//		let item: any = document.querySelectorAll(this);
//		if (item.is('label')) {
//			// Update labels
//			item.attr('for', replaceTemplateIndex(item.attr('for'), newIndex));
//			return;
//		}
//		// Update other fields
//		item.attr('id', replaceTemplateIndex(item.attr('id'), newIndex));
//		item.attr('name', replaceTemplateIndex(item.attr('name'), newIndex));
//	});
//	// Append
//	document.getElementById('subforms-container')!.append(newForm);
//	newForm.addClass('productItem');
//	newForm.removeClass('is-hidden');
//	newForm.find('.remove').click(removeForm);
//}
//window.document.addEventListener("DOMContentLoaded", function () {
//	window.console.log("transaction form");
//	//document.getElementById('productItemAdd')?.click(addForm);
//	//document.getElementById('productItemRemove')?.click(removeForm);
//});


/***/ })

},
/******/ __webpack_require__ => { // webpackRuntimeModules
/******/ var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
/******/ var __webpack_exports__ = (__webpack_exec__("./frontend/src/ts/app.ts"), __webpack_exec__("./frontend/src/js/app.js"));
/******/ }
]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoianMvYXBwLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7O0FBQUFBLE1BQU0sQ0FBQ0MsT0FBUCxDQUFlQyxHQUFmLENBQW1CLG1CQUFuQjs7Ozs7Ozs7Ozs7Ozs7O0FDQUE7Q0FHQTtBQUNBO0FBQ0E7QUFFQTs7QUFDQTtBQUVBRixNQUFNLENBQUNHLFFBQVAsQ0FBZ0JDLGdCQUFoQixDQUFpQyxrQkFBakMsRUFBcUQsWUFBWTtBQUMvREosRUFBQUEsTUFBTSxDQUFDQyxPQUFQLENBQWVDLEdBQWYsQ0FBbUIsYUFBbkI7QUFDRCxDQUZEOzs7Ozs7Ozs7Ozs7QUNWQTs7Ozs7Ozs7Ozs7OztBQ0NBLGtDQUFrQztBQUNsQyw0QkFBNEI7QUFFNUIsS0FBSztBQUNMLDJEQUEyRDtBQUMzRCxnQkFBZ0I7QUFDaEIsSUFBSTtBQUNKLHlEQUF5RDtBQUN6RCwrQ0FBK0M7QUFDL0MsNkNBQTZDO0FBQzdDLEdBQUc7QUFFSCxLQUFLO0FBQ0wsMERBQTBEO0FBQzFELElBQUk7QUFDSix3REFBd0Q7QUFDeEQsbUVBQW1FO0FBRW5FLCtCQUErQjtBQUMvQiwrQkFBK0I7QUFDL0Isb0RBQW9EO0FBQ3BELGtEQUFrRDtBQUNsRCxrQ0FBa0M7QUFFbEMsK0JBQStCO0FBQy9CLFlBQVk7QUFDWixpQkFBaUI7QUFDakIsS0FBSztBQUVMLDREQUE0RDtBQUM1RCwwREFBMEQ7QUFDMUQsMkRBQTJEO0FBQzNELHFCQUFxQjtBQUNyQixzREFBc0Q7QUFDdEQsNENBQTRDO0FBQzVDLCtDQUErQztBQUMvQyxzQ0FBc0M7QUFFdEMsK0JBQStCO0FBQy9CLDhEQUE4RDtBQUM5RCxpQ0FBaUM7QUFFakMsZ0NBQWdDO0FBQ2hDLG1FQUFtRTtBQUNuRSxnQ0FBZ0M7QUFDaEMscURBQXFEO0FBRXJELDRCQUE0QjtBQUM1QixzQkFBc0I7QUFDdEIsZ0VBQWdFO0FBQ2hFLGFBQWE7QUFDYixNQUFNO0FBRU4sMkJBQTJCO0FBQzNCLDZEQUE2RDtBQUM3RCxpRUFBaUU7QUFDakUsT0FBTztBQUNQLE1BQU07QUFDTixHQUFHO0FBRUgsS0FBSztBQUNMLGtCQUFrQjtBQUNsQixJQUFJO0FBQ0osOENBQThDO0FBQzlDLHlEQUF5RDtBQUN6RCxxRkFBcUY7QUFDckYsK0RBQStEO0FBRS9ELHdCQUF3QjtBQUV4QixvQkFBb0I7QUFDcEIsK0JBQStCO0FBQy9CLEdBQUc7QUFFSCxLQUFLO0FBQ0wsbUJBQW1CO0FBQ25CLElBQUk7QUFDSixzQkFBc0I7QUFDdEIsb0VBQW9FO0FBRXBFLGtDQUFrQztBQUNsQyxnREFBZ0Q7QUFDaEQsV0FBVztBQUNYLElBQUk7QUFFSixvQkFBb0I7QUFDcEIsNENBQTRDO0FBQzVDLHFIQUFxSDtBQUVySCx5QkFBeUI7QUFFekIsNkJBQTZCO0FBQzdCLG9EQUFvRDtBQUNwRCxJQUFJO0FBRUosNEJBQTRCO0FBQzVCLHdCQUF3QjtBQUN4QixnRUFBZ0U7QUFDaEUsV0FBVztBQUNYLElBQUk7QUFFSixrQkFBa0I7QUFDbEIsMkNBQTJDO0FBRTNDLDBFQUEwRTtBQUMxRSxtQ0FBbUM7QUFFbkMsdUZBQXVGO0FBQ3ZGLCtCQUErQjtBQUMvQixvREFBb0Q7QUFFcEQsMkJBQTJCO0FBQzNCLHFCQUFxQjtBQUNyQix3RUFBd0U7QUFDeEUsWUFBWTtBQUNaLEtBQUs7QUFFTCwwQkFBMEI7QUFDMUIscUVBQXFFO0FBQ3JFLHlFQUF5RTtBQUN6RSxNQUFNO0FBRU4sWUFBWTtBQUNaLGtFQUFrRTtBQUNsRSxtQ0FBbUM7QUFDbkMsb0NBQW9DO0FBRXBDLDZDQUE2QztBQUM3QyxHQUFHO0FBRUgsb0VBQW9FO0FBQ3BFLDBDQUEwQztBQUMxQywrREFBK0Q7QUFDL0QscUVBQXFFO0FBQ3JFLEtBQUsiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9weXRob24td2VicGFjay1ib2lsZXJwbGF0ZS8uL2Zyb250ZW5kL3NyYy9jb21wb25lbnRzL3NpZGViYXIuanMiLCJ3ZWJwYWNrOi8vcHl0aG9uLXdlYnBhY2stYm9pbGVycGxhdGUvLi9mcm9udGVuZC9zcmMvanMvYXBwLmpzIiwid2VicGFjazovL3B5dGhvbi13ZWJwYWNrLWJvaWxlcnBsYXRlLy4vZnJvbnRlbmQvc3JjL3Njc3MvYXBwLnNjc3MiLCJ3ZWJwYWNrOi8vcHl0aG9uLXdlYnBhY2stYm9pbGVycGxhdGUvLi9mcm9udGVuZC9zcmMvdHMvYXBwLnRzIl0sInNvdXJjZXNDb250ZW50IjpbIndpbmRvdy5jb25zb2xlLmxvZyhcInNpZGViYXIgaXMgbG9hZGVkXCIpO1xuIiwiLy8gVGhpcyBpcyB0aGUgc2NzcyBlbnRyeSBmaWxlXG5pbXBvcnQgXCIuLi9zY3NzL2FwcC5zY3NzXCI7XG5cbi8vIFdlIGNhbiBpbXBvcnQgQm9vdHN0cmFwIEpTIGluc3RlYWQgb2YgdGhlIENETiBsaW5rLCBpZiB5b3UgZG8gbm90IHVzZVxuLy8gQm9vdHN0cmFwLCBwbGVhc2UgZmVlbCBmcmVlIHRvIHJlbW92ZSBpdC5cbi8vaW1wb3J0IFwiYm9vdHN0cmFwL2Rpc3QvanMvYm9vdHN0cmFwLmJ1bmRsZVwiO1xuXG4vLyBXZSBjYW4gaW1wb3J0IG90aGVyIEpTIGZpbGUgYXMgd2UgbGlrZVxuaW1wb3J0IFwiLi4vY29tcG9uZW50cy9zaWRlYmFyXCI7XG5cbndpbmRvdy5kb2N1bWVudC5hZGRFdmVudExpc3RlbmVyKFwiRE9NQ29udGVudExvYWRlZFwiLCBmdW5jdGlvbiAoKSB7XG4gIHdpbmRvdy5jb25zb2xlLmxvZyhcImRvbSByZWFkeSAxXCIpO1xufSk7XG4iLCIvLyBleHRyYWN0ZWQgYnkgbWluaS1jc3MtZXh0cmFjdC1wbHVnaW5cbmV4cG9ydCB7fTsiLCJcbi8vLy8gY29uc3QgSURfUkU6IGFueSA9IC8oLSlfKC0pLztcbi8vY29uc3QgSURfUkU6IGFueSA9IC8oLSlfLztcblxuLy8vKipcbi8vKiBSZXBsYWNlIHRoZSB0ZW1wbGF0ZSBpbmRleCBvZiBhbiBlbGVtZW50ICgtXy0pIHdpdGggdGhlXG4vLyogZ2l2ZW4gaW5kZXguXG4vLyovXG4vL2Z1bmN0aW9uIHJlcGxhY2VUZW1wbGF0ZUluZGV4KHZhbHVlOiBhbnksIGluZGV4OiBhbnkpIHtcbi8vXHQvLyB2YWx1ZS5yZXBsYWNlKElEX1JFLCAnJDEnICsgaW5kZXggKyAnJDInKVxuLy9cdHJldHVybiB2YWx1ZS5yZXBsYWNlKElEX1JFLCAnJDEnICsgaW5kZXgpO1xuLy99XG5cbi8vLyoqXG4vLyogQWRqdXN0IHRoZSBpbmRpY2VzIG9mIGZvcm0gZmllbGRzIHdoZW4gcmVtb3ZpbmcgaXRlbXMuXG4vLyovXG4vL2Z1bmN0aW9uIGFkanVzdEluZGljZXModGhpczogYW55LCByZW1vdmVkSW5kZXg6IGFueSkge1xuLy9cdGxldCBmb3JtczogYW55ID0gZG9jdW1lbnQuZ2V0RWxlbWVudHNCeUNsYXNzTmFtZSgncHJvZHVjdEl0ZW0nKTtcblxuLy9cdGZvcm1zLmVhY2goIChpOiBudW1iZXIpID0+IHtcbi8vXHRcdC8vIGxldCBmb3JtOiBhbnkgPSAkKHRoaXMpO1xuLy9cdFx0bGV0IGZvcm06IGFueSA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwodGhpcyk7XG4vL1x0XHRsZXQgaW5kZXg6IGFueSA9IHBhcnNlSW50KGZvcm0uZGF0YSgnaW5kZXgnKSk7XG4vL1x0XHRsZXQgbmV3SW5kZXg6IGFueSA9IGluZGV4IC0gMTtcblxuLy9cdFx0aWYgKGluZGV4IDwgcmVtb3ZlZEluZGV4KSB7XG4vL1x0XHRcdC8vIFNraXBcbi8vXHRcdFx0cmV0dXJuIHRydWU7XG4vL1x0XHR9XG5cbi8vXHRcdC8vIFRoaXMgd2lsbCByZXBsYWNlIHRoZSBvcmlnaW5hbCBpbmRleCB3aXRoIHRoZSBuZXcgb25lXG4vL1x0XHQvLyBvbmx5IGlmIGl0IGlzIGZvdW5kIGluIHRoZSBmb3JtYXQgLW51bS0sIHByZXZlbnRpbmdcbi8vXHRcdC8vIGFjY2lkZW50YWwgcmVwbGFjaW5nIG9mIGZpZWxkcyB0aGF0IG1heSBoYXZlIG51bWJlcnNcbi8vXHRcdC8vIGludGhlaXIgbmFtZXMuXG4vL1x0XHQvLyBsZXQgcmVnZXg6IGFueSA9IG5ldyBSZWdFeHAoJygtKScraW5kZXgrJygtKScpO1xuLy9cdFx0Ly8gbGV0IHJlcFZhbDogYW55ID0gJyQxJytuZXdJbmRleCsnJDInO1xuLy9cdFx0bGV0IHJlZ2V4OiBhbnkgPSBuZXcgUmVnRXhwKCcoLSknICsgaW5kZXgpO1xuLy9cdFx0bGV0IHJlcFZhbDogYW55ID0gJyQxJyArIG5ld0luZGV4O1xuXG4vL1x0XHQvLyBDaGFuZ2UgSUQgaW4gZm9ybSBpdHNlbGZcbi8vXHRcdGZvcm0uYXR0cignaWQnLCBmb3JtLmF0dHIoJ2lkJykucmVwbGFjZShpbmRleCwgbmV3SW5kZXgpKTtcbi8vXHRcdGZvcm0uZGF0YSgnaW5kZXgnLCBuZXdJbmRleCk7XG5cbi8vXHRcdC8vIENoYW5nZSBJRHMgaW4gZm9ybSBmaWVsZHNcbi8vXHRcdGZvcm0uZmluZCgnbGFiZWwsIGlucHV0LCBzZWxlY3QsIHRleHRhcmVhJykuZWFjaCggKGo6IGFueSkgPT4ge1xuLy9cdFx0XHQvLyBsZXQgaXRlbTogYW55ID0gJCh0aGlzKTtcbi8vXHRcdFx0bGV0IGl0ZW06IGFueSA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwodGhpcyk7XG5cbi8vXHRcdFx0aWYgKGl0ZW0uaXMoJ2xhYmVsJykpIHtcbi8vXHRcdFx0XHQvLyBVcGRhdGUgbGFiZWxzXG4vL1x0XHRcdFx0aXRlbS5hdHRyKCdmb3InLCBpdGVtLmF0dHIoJ2ZvcicpLnJlcGxhY2UocmVnZXgsIHJlcFZhbCkpO1xuLy9cdFx0XHRcdHJldHVybjtcbi8vXHRcdFx0fVxuXG4vL1x0XHRcdC8vIFVwZGF0ZSBvdGhlciBmaWVsZHNcbi8vXHRcdFx0aXRlbS5hdHRyKCdpZCcsIGl0ZW0uYXR0cignaWQnKS5yZXBsYWNlKHJlZ2V4LCByZXBWYWwpKTtcbi8vXHRcdFx0aXRlbS5hdHRyKCduYW1lJywgaXRlbS5hdHRyKCduYW1lJykucmVwbGFjZShyZWdleCwgcmVwVmFsKSk7XG4vL1x0XHR9KTtcbi8vXHR9KTtcbi8vfVxuXG4vLy8qKlxuLy8qIFJlbW92ZSBhIGZvcm0uXG4vLyovXG4vL2Z1bmN0aW9uIHJlbW92ZUZvcm0ocHJvZHVjdEl0ZW1JbmRleDogYW55KSB7XG4vL1x0Ly8gbGV0IHJlbW92ZWRGb3JtOiBhbnkgPSAkKHRoaXMpLmNsb3Nlc3QoJy5zdWJmb3JtJyk7XG4vL1x0bGV0IHJlbW92ZWRGb3JtOiBhbnkgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgncHJvZHVjdEl0ZW0tJyArIHByb2R1Y3RJdGVtSW5kZXgpO1xuLy9cdGxldCByZW1vdmVkSW5kZXg6IGFueSA9IHBhcnNlSW50KHJlbW92ZWRGb3JtLmRhdGEoJ2luZGV4JykpO1xuXG4vL1x0cmVtb3ZlZEZvcm0ucmVtb3ZlKCk7XG5cbi8vXHQvLyBVcGRhdGUgaW5kaWNlc1xuLy9cdGFkanVzdEluZGljZXMocmVtb3ZlZEluZGV4KTtcbi8vfVxuXG4vLy8qKlxuLy8qIEFkZCBhIG5ldyBmb3JtLlxuLy8qL1xuLy9mdW5jdGlvbiBhZGRGb3JtKCkge1xuLy9cdGxldCB0ZW1wbGF0ZUZvcm06IGFueSA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdwcm9kdWN0SXRlbS1fJyk7XG5cbi8vXHRpZiAodGVtcGxhdGVGb3JtLmxlbmd0aCA9PSAwKSB7XG4vL1x0XHRjb25zb2xlLmxvZygnW0VSUk9SXSBDYW5ub3QgZmluZCB0ZW1wbGF0ZScpO1xuLy9cdFx0cmV0dXJuO1xuLy9cdH1cblxuLy9cdC8vIEdldCBMYXN0IGluZGV4XG4vL1x0ZG9jdW1lbnQucXVlcnlTZWxlY3RvckFsbCgncHJvZHVjdEl0ZW0nKTtcbi8vXHRsZXQgbGFzdEZvcm06IGFueSA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJ3Byb2R1Y3RJdGVtJylbZG9jdW1lbnQucXVlcnlTZWxlY3RvckFsbCgncHJvZHVjdEl0ZW0nKS5sZW5ndGggLSAxXTtcblxuLy9cdGxldCBuZXdJbmRleDogYW55ID0gMDtcblxuLy9cdGlmIChsYXN0Rm9ybS5sZW5ndGggPiAwKSB7XG4vL1x0XHRuZXdJbmRleCA9IHBhcnNlSW50KGxhc3RGb3JtLmRhdGEoJ2luZGV4JykpICsgMTtcbi8vXHR9XG5cbi8vXHQvLyBNYXhpbXVtIG9mIDIwIHN1YmZvcm1zXG4vL1x0aWYgKG5ld0luZGV4ID49IDIwKSB7XG4vL1x0XHRjb25zb2xlLmxvZygnW1dBUk5JTkddIFJlYWNoZWQgbWF4aW11bSBudW1iZXIgb2YgZWxlbWVudHMnKTtcbi8vXHRcdHJldHVybjtcbi8vXHR9XG5cbi8vXHQvLyBBZGQgZWxlbWVudHNcbi8vXHRsZXQgbmV3Rm9ybTogYW55ID0gdGVtcGxhdGVGb3JtLmNsb25lKCk7XG5cbi8vXHRuZXdGb3JtLmF0dHIoJ2lkJywgcmVwbGFjZVRlbXBsYXRlSW5kZXgobmV3Rm9ybS5hdHRyKCdpZCcpLCBuZXdJbmRleCkpO1xuLy9cdG5ld0Zvcm0uZGF0YSgnaW5kZXgnLCBuZXdJbmRleCk7XG5cbi8vXHRuZXdGb3JtLmZpbmQoJ2xhYmVsLCBpbnB1dCwgc2VsZWN0LCB0ZXh0YXJlYScpLmVhY2goZnVuY3Rpb24gKHRoaXM6IGFueSwgaWR4OiBhbnkpIHtcbi8vXHRcdC8vIGxldCBpdGVtOiBhbnkgPSAkKHRoaXMpO1xuLy9cdFx0bGV0IGl0ZW06IGFueSA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwodGhpcyk7XG5cbi8vXHRcdGlmIChpdGVtLmlzKCdsYWJlbCcpKSB7XG4vL1x0XHRcdC8vIFVwZGF0ZSBsYWJlbHNcbi8vXHRcdFx0aXRlbS5hdHRyKCdmb3InLCByZXBsYWNlVGVtcGxhdGVJbmRleChpdGVtLmF0dHIoJ2ZvcicpLCBuZXdJbmRleCkpO1xuLy9cdFx0XHRyZXR1cm47XG4vL1x0XHR9XG5cbi8vXHRcdC8vIFVwZGF0ZSBvdGhlciBmaWVsZHNcbi8vXHRcdGl0ZW0uYXR0cignaWQnLCByZXBsYWNlVGVtcGxhdGVJbmRleChpdGVtLmF0dHIoJ2lkJyksIG5ld0luZGV4KSk7XG4vL1x0XHRpdGVtLmF0dHIoJ25hbWUnLCByZXBsYWNlVGVtcGxhdGVJbmRleChpdGVtLmF0dHIoJ25hbWUnKSwgbmV3SW5kZXgpKTtcbi8vXHR9KTtcblxuLy9cdC8vIEFwcGVuZFxuLy9cdGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdzdWJmb3Jtcy1jb250YWluZXInKSEuYXBwZW5kKG5ld0Zvcm0pO1xuLy9cdG5ld0Zvcm0uYWRkQ2xhc3MoJ3Byb2R1Y3RJdGVtJyk7XG4vL1x0bmV3Rm9ybS5yZW1vdmVDbGFzcygnaXMtaGlkZGVuJyk7XG5cbi8vXHRuZXdGb3JtLmZpbmQoJy5yZW1vdmUnKS5jbGljayhyZW1vdmVGb3JtKTtcbi8vfVxuXG4vL3dpbmRvdy5kb2N1bWVudC5hZGRFdmVudExpc3RlbmVyKFwiRE9NQ29udGVudExvYWRlZFwiLCBmdW5jdGlvbiAoKSB7XG4vL1x0d2luZG93LmNvbnNvbGUubG9nKFwidHJhbnNhY3Rpb24gZm9ybVwiKTtcbi8vXHQvL2RvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdwcm9kdWN0SXRlbUFkZCcpPy5jbGljayhhZGRGb3JtKTtcbi8vXHQvL2RvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdwcm9kdWN0SXRlbVJlbW92ZScpPy5jbGljayhyZW1vdmVGb3JtKTtcbi8vfSk7Il0sIm5hbWVzIjpbIndpbmRvdyIsImNvbnNvbGUiLCJsb2ciLCJkb2N1bWVudCIsImFkZEV2ZW50TGlzdGVuZXIiXSwic291cmNlUm9vdCI6IiJ9