(self["webpackChunkpython_webpack_boilerplate"] = self["webpackChunkpython_webpack_boilerplate"] || []).push([["app"],{

/***/ "./frontend/src/components/sidebar.js":
/*!********************************************!*\
  !*** ./frontend/src/components/sidebar.js ***!
  \********************************************/
/***/ (() => {



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


window.document.addEventListener("DOMContentLoaded", function() {
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
    //Swal.fire('Hi from webpack!');
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
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoianMvYXBwLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQzBCO0FBT0s7QUFFL0IsT0FBTyxTQUFTLGlCQUFpQixvQkFBb0IsV0FBWTtBQUMvRCxTQUFPLFFBQVEsSUFBSSxhQUFhO0FBRWxDLENBQUM7Ozs7Ozs7Ozs7Ozs7QUNiRDs7Ozs7Ozs7Ozs7OztBQ1NDLENBQUM7QUFJRixNQUFNLENBQUMsUUFBUSxDQUFDLGdCQUFnQixDQUFDLGtCQUFrQixFQUFFO0lBRXBELGdDQUFnQztJQUVoQyw2QkFBNkI7SUFDN0IsMkNBQTJDO0lBQzNDLCtDQUErQztJQUUvQyw4Q0FBOEM7SUFDOUMsTUFBTSxDQUFDLFlBQVksR0FBRyxVQUFTLElBQVMsRUFBRSxHQUFXO1FBQ3BELElBQUksTUFBTSxDQUFDLE9BQU8sQ0FBQyxpQ0FBaUMsQ0FBQztZQUFFLE1BQU0sQ0FBQyxRQUFRLENBQUMsSUFBSSxHQUFHLEdBQUcsQ0FBQztJQUNuRixDQUFDO0lBRUQsaUNBQWlDO0lBQ2pDLDJCQUEyQjtJQUMzQiw0QkFBNEI7SUFDNUIsTUFBTSxDQUFDLFlBQVksR0FBRyxVQUFTLElBQVMsRUFBRSxHQUFXO1FBQ3BELElBQUksTUFBTSxDQUFDLE9BQU8sQ0FBQyxrQ0FBa0MsR0FBRyxJQUFJLEdBQUcsR0FBRyxDQUFDO1lBQUUsTUFBTSxDQUFDLFFBQVEsQ0FBQyxJQUFJLEdBQUcsR0FBRyxDQUFDO0lBQ2pHLENBQUM7SUFFRCxtQ0FBbUM7SUFDbkMsTUFBTSxDQUFDLG1CQUFtQixHQUFHLFVBQVMsSUFBUyxFQUFFLEdBQVc7UUFDM0QsSUFBSSxNQUFNLENBQUMsT0FBTyxDQUFDLHVDQUF1QyxHQUFHLElBQUksR0FBRyxHQUFHLENBQUM7WUFBRSxNQUFNLENBQUMsUUFBUSxDQUFDLElBQUksR0FBRyxHQUFHLENBQUM7SUFDdEcsQ0FBQztJQUVELDRCQUE0QjtJQUM1QixNQUFNLENBQUMsWUFBWSxHQUFHLFVBQVMsSUFBUyxFQUFFLEdBQVc7UUFDcEQsSUFBSSxNQUFNLENBQUMsT0FBTyxDQUFDLHNDQUFzQyxHQUFHLElBQUksR0FBRyxHQUFHLENBQUM7WUFBRSxNQUFNLENBQUMsUUFBUSxDQUFDLElBQUksR0FBRyxHQUFHLENBQUM7SUFDckcsQ0FBQztBQUVGLENBQUMsQ0FBQyxDQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vcHl0aG9uLXdlYnBhY2stYm9pbGVycGxhdGUvLi9mcm9udGVuZC9zcmMvanMvYXBwLmpzIiwid2VicGFjazovL3B5dGhvbi13ZWJwYWNrLWJvaWxlcnBsYXRlLy4vZnJvbnRlbmQvc3JjL3Njc3MvYXBwLnNjc3MiLCJ3ZWJwYWNrOi8vcHl0aG9uLXdlYnBhY2stYm9pbGVycGxhdGUvLi9mcm9udGVuZC9zcmMvdHMvYXBwLnRzIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIFRoaXMgaXMgdGhlIHNjc3MgZW50cnkgZmlsZVxuaW1wb3J0IFwiLi4vc2Nzcy9hcHAuc2Nzc1wiO1xuXG4vLyBXZSBjYW4gaW1wb3J0IEJvb3RzdHJhcCBKUyBpbnN0ZWFkIG9mIHRoZSBDRE4gbGluaywgaWYgeW91IGRvIG5vdCB1c2Vcbi8vIEJvb3RzdHJhcCwgcGxlYXNlIGZlZWwgZnJlZSB0byByZW1vdmUgaXQuXG4vL2ltcG9ydCBcImJvb3RzdHJhcC9kaXN0L2pzL2Jvb3RzdHJhcC5idW5kbGVcIjtcblxuLy8gV2UgY2FuIGltcG9ydCBvdGhlciBKUyBmaWxlIGFzIHdlIGxpa2VcbmltcG9ydCBcIi4uL2NvbXBvbmVudHMvc2lkZWJhclwiO1xuXG53aW5kb3cuZG9jdW1lbnQuYWRkRXZlbnRMaXN0ZW5lcihcIkRPTUNvbnRlbnRMb2FkZWRcIiwgZnVuY3Rpb24gKCkge1xuICB3aW5kb3cuY29uc29sZS5sb2coXCJkb20gcmVhZHkgMVwiKTtcblxufSk7XG4iLCIvLyBleHRyYWN0ZWQgYnkgbWluaS1jc3MtZXh0cmFjdC1wbHVnaW5cbmV4cG9ydCB7fTsiLCJleHBvcnQgeyB9XG5cbmRlY2xhcmUgZ2xvYmFsIHtcblx0aW50ZXJmYWNlIFdpbmRvdyB7XG5cdFx0b25EZWxldGVEYXRhOiBhbnk7IC8vIChkYXRhOiBhbnksIHVybD86IHN0cmluZykgPT4gdm9pZFxuXHRcdG9uRGVsZXRlRHJ1ZzogYW55OyAvLyAoZGF0YTogYW55LCB1cmw/OiBzdHJpbmcpID0+IHZvaWRcblx0XHRvbkRlbGV0ZVRyYW5zYWN0aW9uOiBhbnk7IC8vIChkYXRhOiBhbnksIHVybD86IHN0cmluZykgPT4gdm9pZFxuXHRcdG9uRGVsZXRlVXNlcjogYW55OyAvLyAoZGF0YTogYW55LCB1cmw/OiBzdHJpbmcpID0+IHZvaWRcblx0fVxufTtcblxuaW1wb3J0IFN3YWwgZnJvbSAnc3dlZXRhbGVydDInO1xuXG53aW5kb3cuZG9jdW1lbnQuYWRkRXZlbnRMaXN0ZW5lcihcIkRPTUNvbnRlbnRMb2FkZWRcIiwgZnVuY3Rpb24gKCkge1xuXG5cdC8vU3dhbC5maXJlKCdIaSBmcm9tIHdlYnBhY2shJyk7XG5cblx0Ly92YXIgdmV4ID0gcmVxdWlyZSgndmV4LWpzJylcblx0Ly92ZXgucmVnaXN0ZXJQbHVnaW4ocmVxdWlyZSgndmV4LWRpYWxvZycpKVxuXHQvL3ZleC5kZWZhdWx0T3B0aW9ucy5jbGFzc05hbWUgPSAndmV4LXRoZW1lLW9zJ1xuXG5cdC8vdmV4LmRpYWxvZy5hbGVydCgnSSB3YXMgbWFkZSBieSBhIHBsdWdpbiEnKTtcblx0d2luZG93Lm9uRGVsZXRlRGF0YSA9IGZ1bmN0aW9uKGRhdGE6IGFueSwgdXJsOiBzdHJpbmcpOiB2b2lkIHtcblx0XHRpZiAod2luZG93LmNvbmZpcm0oXCJZYWtpbiBpbmdpbiBtZW5naGFwdXMgZGF0YSBpbmk/XCIpKSB3aW5kb3cubG9jYXRpb24uaHJlZiA9IHVybDtcblx0fVxuXG5cdC8qKiBEYXNoYm9hcmQgcGFnZWBzIGZ1bmN0aW9ucyAqL1xuXHQvKiogR1NQIHBhZ2VgcyBmdW5jdGlvbnMgKi9cblx0LyoqIERydWcgcGFnZWBzIGZ1bmN0aW9ucyAqL1xuXHR3aW5kb3cub25EZWxldGVEcnVnID0gZnVuY3Rpb24oZGF0YTogYW55LCB1cmw6IHN0cmluZyk6IHZvaWQge1xuXHRcdGlmICh3aW5kb3cuY29uZmlybShcIllha2luIGluZ2luIG1lbmdoYXB1cyBkYXRhIG9iYXQgXCIgKyBkYXRhICsgXCI/XCIpKSB3aW5kb3cubG9jYXRpb24uaHJlZiA9IHVybDtcblx0fVxuXG5cdC8qKiBUcmFuc2FjdGlvbiBwYWdlYHMgZnVuY3Rpb25zICovXG5cdHdpbmRvdy5vbkRlbGV0ZVRyYW5zYWN0aW9uID0gZnVuY3Rpb24oZGF0YTogYW55LCB1cmw6IHN0cmluZyk6IHZvaWQge1xuXHRcdGlmICh3aW5kb3cuY29uZmlybShcIllha2luIGluZ2luIG1lbmdoYXB1cyBkYXRhIHRyYW5zYWtzaSBcIiArIGRhdGEgKyBcIj9cIikpIHdpbmRvdy5sb2NhdGlvbi5ocmVmID0gdXJsO1xuXHR9XG5cblx0LyoqIFVzZXIgcGFnZWBzIGZ1bmN0aW9ucyAqL1xuXHR3aW5kb3cub25EZWxldGVVc2VyID0gZnVuY3Rpb24oZGF0YTogYW55LCB1cmw6IHN0cmluZyk6IHZvaWQge1xuXHRcdGlmICh3aW5kb3cuY29uZmlybShcIllha2luIGluZ2luIG1lbmdoYXB1cyBkYXRhIHBlbmdndW5hIFwiICsgZGF0YSArIFwiP1wiKSkgd2luZG93LmxvY2F0aW9uLmhyZWYgPSB1cmw7XG5cdH1cblxufSk7Il0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9