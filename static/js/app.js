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
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
;
window.document.addEventListener("DOMContentLoaded", function () {
    //var vex = require('vex-js')
    //vex.registerPlugin(require('vex-dialog'))
    //vex.defaultOptions.className = 'vex-theme-os'
    //vex.dialog.alert('I was made by a plugin!');
    window.onDeleteData = function (data, url) {
        if (window.confirm("Yakin ingin menghapus data ini?"))
            window.location.href = url;
    };
    /** Dashboard page`s functions */
    /** GSP page`s functions */
    /** Drug page`s functions */
    window.onDeleteDrug = function (data, url) {
        if (window.confirm("Yakin ingin menghapus data obat " + data + "?"))
            window.location.href = url;
    };
    /** Transaction page`s functions */
    window.onDeleteTransaction = function (data, url) {
        if (window.confirm("Yakin ingin menghapus data transaksi " + data + "?"))
            window.location.href = url;
    };
    /** User page`s functions */
    window.onDeleteUser = function (data, url) {
        if (window.confirm("Yakin ingin menghapus data pengguna " + data + "?"))
            window.location.href = url;
    };
});



/***/ })

},
/******/ __webpack_require__ => { // webpackRuntimeModules
/******/ var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
/******/ var __webpack_exports__ = (__webpack_exec__("./frontend/src/ts/app.ts"), __webpack_exec__("./frontend/src/js/app.js"));
/******/ }
]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoianMvYXBwLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7O0FBQUFBLE1BQU0sQ0FBQ0MsT0FBUCxDQUFlQyxHQUFmLENBQW1CLG1CQUFuQjs7Ozs7Ozs7Ozs7Ozs7O0FDQUE7Q0FHQTtBQUNBO0FBQ0E7QUFFQTs7QUFDQTtBQUVBRixNQUFNLENBQUNHLFFBQVAsQ0FBZ0JDLGdCQUFoQixDQUFpQyxrQkFBakMsRUFBcUQsWUFBWTtBQUMvREosRUFBQUEsTUFBTSxDQUFDQyxPQUFQLENBQWVDLEdBQWYsQ0FBbUIsYUFBbkI7QUFFRCxDQUhEOzs7Ozs7Ozs7Ozs7QUNWQTs7Ozs7Ozs7Ozs7OztBQ1NDLENBQUM7QUFFRixNQUFNLENBQUMsUUFBUSxDQUFDLGdCQUFnQixDQUFDLGtCQUFrQixFQUFFO0lBRXBELDZCQUE2QjtJQUM3QiwyQ0FBMkM7SUFDM0MsK0NBQStDO0lBRS9DLDhDQUE4QztJQUM5QyxNQUFNLENBQUMsWUFBWSxHQUFHLFVBQVMsSUFBUyxFQUFFLEdBQVc7UUFDcEQsSUFBSSxNQUFNLENBQUMsT0FBTyxDQUFDLGlDQUFpQyxDQUFDO1lBQUUsTUFBTSxDQUFDLFFBQVEsQ0FBQyxJQUFJLEdBQUcsR0FBRyxDQUFDO0lBQ25GLENBQUM7SUFFRCxpQ0FBaUM7SUFDakMsMkJBQTJCO0lBQzNCLDRCQUE0QjtJQUM1QixNQUFNLENBQUMsWUFBWSxHQUFHLFVBQVMsSUFBUyxFQUFFLEdBQVc7UUFDcEQsSUFBSSxNQUFNLENBQUMsT0FBTyxDQUFDLGtDQUFrQyxHQUFHLElBQUksR0FBRyxHQUFHLENBQUM7WUFBRSxNQUFNLENBQUMsUUFBUSxDQUFDLElBQUksR0FBRyxHQUFHLENBQUM7SUFDakcsQ0FBQztJQUVELG1DQUFtQztJQUNuQyxNQUFNLENBQUMsbUJBQW1CLEdBQUcsVUFBUyxJQUFTLEVBQUUsR0FBVztRQUMzRCxJQUFJLE1BQU0sQ0FBQyxPQUFPLENBQUMsdUNBQXVDLEdBQUcsSUFBSSxHQUFHLEdBQUcsQ0FBQztZQUFFLE1BQU0sQ0FBQyxRQUFRLENBQUMsSUFBSSxHQUFHLEdBQUcsQ0FBQztJQUN0RyxDQUFDO0lBRUQsNEJBQTRCO0lBQzVCLE1BQU0sQ0FBQyxZQUFZLEdBQUcsVUFBUyxJQUFTLEVBQUUsR0FBVztRQUNwRCxJQUFJLE1BQU0sQ0FBQyxPQUFPLENBQUMsc0NBQXNDLEdBQUcsSUFBSSxHQUFHLEdBQUcsQ0FBQztZQUFFLE1BQU0sQ0FBQyxRQUFRLENBQUMsSUFBSSxHQUFHLEdBQUcsQ0FBQztJQUNyRyxDQUFDO0FBRUYsQ0FBQyxDQUFDLENBQUMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9weXRob24td2VicGFjay1ib2lsZXJwbGF0ZS8uL2Zyb250ZW5kL3NyYy9jb21wb25lbnRzL3NpZGViYXIuanMiLCJ3ZWJwYWNrOi8vcHl0aG9uLXdlYnBhY2stYm9pbGVycGxhdGUvLi9mcm9udGVuZC9zcmMvanMvYXBwLmpzIiwid2VicGFjazovL3B5dGhvbi13ZWJwYWNrLWJvaWxlcnBsYXRlLy4vZnJvbnRlbmQvc3JjL3Njc3MvYXBwLnNjc3MiLCJ3ZWJwYWNrOi8vcHl0aG9uLXdlYnBhY2stYm9pbGVycGxhdGUvLi9mcm9udGVuZC9zcmMvdHMvYXBwLnRzIl0sInNvdXJjZXNDb250ZW50IjpbIndpbmRvdy5jb25zb2xlLmxvZyhcInNpZGViYXIgaXMgbG9hZGVkXCIpO1xuIiwiLy8gVGhpcyBpcyB0aGUgc2NzcyBlbnRyeSBmaWxlXG5pbXBvcnQgXCIuLi9zY3NzL2FwcC5zY3NzXCI7XG5cbi8vIFdlIGNhbiBpbXBvcnQgQm9vdHN0cmFwIEpTIGluc3RlYWQgb2YgdGhlIENETiBsaW5rLCBpZiB5b3UgZG8gbm90IHVzZVxuLy8gQm9vdHN0cmFwLCBwbGVhc2UgZmVlbCBmcmVlIHRvIHJlbW92ZSBpdC5cbi8vaW1wb3J0IFwiYm9vdHN0cmFwL2Rpc3QvanMvYm9vdHN0cmFwLmJ1bmRsZVwiO1xuXG4vLyBXZSBjYW4gaW1wb3J0IG90aGVyIEpTIGZpbGUgYXMgd2UgbGlrZVxuaW1wb3J0IFwiLi4vY29tcG9uZW50cy9zaWRlYmFyXCI7XG5cbndpbmRvdy5kb2N1bWVudC5hZGRFdmVudExpc3RlbmVyKFwiRE9NQ29udGVudExvYWRlZFwiLCBmdW5jdGlvbiAoKSB7XG4gIHdpbmRvdy5jb25zb2xlLmxvZyhcImRvbSByZWFkeSAxXCIpO1xuXG59KTtcbiIsIi8vIGV4dHJhY3RlZCBieSBtaW5pLWNzcy1leHRyYWN0LXBsdWdpblxuZXhwb3J0IHt9OyIsImV4cG9ydCB7IH1cblxuZGVjbGFyZSBnbG9iYWwge1xuXHRpbnRlcmZhY2UgV2luZG93IHtcblx0XHRvbkRlbGV0ZURhdGE6IGFueTsgLy8gKGRhdGE6IGFueSwgdXJsPzogc3RyaW5nKSA9PiB2b2lkXG5cdFx0b25EZWxldGVEcnVnOiBhbnk7IC8vIChkYXRhOiBhbnksIHVybD86IHN0cmluZykgPT4gdm9pZFxuXHRcdG9uRGVsZXRlVHJhbnNhY3Rpb246IGFueTsgLy8gKGRhdGE6IGFueSwgdXJsPzogc3RyaW5nKSA9PiB2b2lkXG5cdFx0b25EZWxldGVVc2VyOiBhbnk7IC8vIChkYXRhOiBhbnksIHVybD86IHN0cmluZykgPT4gdm9pZFxuXHR9XG59O1xuXG53aW5kb3cuZG9jdW1lbnQuYWRkRXZlbnRMaXN0ZW5lcihcIkRPTUNvbnRlbnRMb2FkZWRcIiwgZnVuY3Rpb24gKCkge1xuXG5cdC8vdmFyIHZleCA9IHJlcXVpcmUoJ3ZleC1qcycpXG5cdC8vdmV4LnJlZ2lzdGVyUGx1Z2luKHJlcXVpcmUoJ3ZleC1kaWFsb2cnKSlcblx0Ly92ZXguZGVmYXVsdE9wdGlvbnMuY2xhc3NOYW1lID0gJ3ZleC10aGVtZS1vcydcblxuXHQvL3ZleC5kaWFsb2cuYWxlcnQoJ0kgd2FzIG1hZGUgYnkgYSBwbHVnaW4hJyk7XG5cdHdpbmRvdy5vbkRlbGV0ZURhdGEgPSBmdW5jdGlvbihkYXRhOiBhbnksIHVybDogc3RyaW5nKTogdm9pZCB7XG5cdFx0aWYgKHdpbmRvdy5jb25maXJtKFwiWWFraW4gaW5naW4gbWVuZ2hhcHVzIGRhdGEgaW5pP1wiKSkgd2luZG93LmxvY2F0aW9uLmhyZWYgPSB1cmw7XG5cdH1cblxuXHQvKiogRGFzaGJvYXJkIHBhZ2VgcyBmdW5jdGlvbnMgKi9cblx0LyoqIEdTUCBwYWdlYHMgZnVuY3Rpb25zICovXG5cdC8qKiBEcnVnIHBhZ2VgcyBmdW5jdGlvbnMgKi9cblx0d2luZG93Lm9uRGVsZXRlRHJ1ZyA9IGZ1bmN0aW9uKGRhdGE6IGFueSwgdXJsOiBzdHJpbmcpOiB2b2lkIHtcblx0XHRpZiAod2luZG93LmNvbmZpcm0oXCJZYWtpbiBpbmdpbiBtZW5naGFwdXMgZGF0YSBvYmF0IFwiICsgZGF0YSArIFwiP1wiKSkgd2luZG93LmxvY2F0aW9uLmhyZWYgPSB1cmw7XG5cdH1cblxuXHQvKiogVHJhbnNhY3Rpb24gcGFnZWBzIGZ1bmN0aW9ucyAqL1xuXHR3aW5kb3cub25EZWxldGVUcmFuc2FjdGlvbiA9IGZ1bmN0aW9uKGRhdGE6IGFueSwgdXJsOiBzdHJpbmcpOiB2b2lkIHtcblx0XHRpZiAod2luZG93LmNvbmZpcm0oXCJZYWtpbiBpbmdpbiBtZW5naGFwdXMgZGF0YSB0cmFuc2Frc2kgXCIgKyBkYXRhICsgXCI/XCIpKSB3aW5kb3cubG9jYXRpb24uaHJlZiA9IHVybDtcblx0fVxuXG5cdC8qKiBVc2VyIHBhZ2VgcyBmdW5jdGlvbnMgKi9cblx0d2luZG93Lm9uRGVsZXRlVXNlciA9IGZ1bmN0aW9uKGRhdGE6IGFueSwgdXJsOiBzdHJpbmcpOiB2b2lkIHtcblx0XHRpZiAod2luZG93LmNvbmZpcm0oXCJZYWtpbiBpbmdpbiBtZW5naGFwdXMgZGF0YSBwZW5nZ3VuYSBcIiArIGRhdGEgKyBcIj9cIikpIHdpbmRvdy5sb2NhdGlvbi5ocmVmID0gdXJsO1xuXHR9XG5cbn0pOyJdLCJuYW1lcyI6WyJ3aW5kb3ciLCJjb25zb2xlIiwibG9nIiwiZG9jdW1lbnQiLCJhZGRFdmVudExpc3RlbmVyIl0sInNvdXJjZVJvb3QiOiIifQ==