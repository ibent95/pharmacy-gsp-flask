/*! For license information please see vex.combined.js.LICENSE.txt */
!function(e){"object"==typeof exports&&"undefined"!=typeof module?module.exports=e():"function"==typeof define&&define.amd?define([],e):("undefined"!=typeof window?window:"undefined"!=typeof global?global:"undefined"!=typeof self?self:this).vex=e()}((function(){return function e(t,n,o){function i(a,s){if(!n[a]){if(!t[a]){var l="function"==typeof require&&require;if(!s&&l)return l(a,!0);if(r)return r(a,!0);var c=new Error("Cannot find module '"+a+"'");throw c.code="MODULE_NOT_FOUND",c}var u=n[a]={exports:{}};t[a][0].call(u.exports,(function(e){return i(t[a][1][e]||e)}),u,u.exports,e,t,n,o)}return n[a].exports}for(var r="function"==typeof require&&require,a=0;a<o.length;a++)i(o[a]);return i}({1:[function(e,t,n){"document"in window.self&&((!("classList"in document.createElement("_"))||document.createElementNS&&!("classList"in document.createElementNS("http://www.w3.org/2000/svg","g")))&&function(e){"use strict";if("Element"in e){var t="classList",n=e.Element.prototype,o=Object,i=String.prototype.trim||function(){return this.replace(/^\s+|\s+$/g,"")},r=Array.prototype.indexOf||function(e){for(var t=0,n=this.length;t<n;t++)if(t in this&&this[t]===e)return t;return-1},a=function(e,t){this.name=e,this.code=DOMException[e],this.message=t},s=function(e,t){if(""===t)throw new a("SYNTAX_ERR","An invalid or illegal string was specified");if(/\s/.test(t))throw new a("INVALID_CHARACTER_ERR","String contains an invalid character");return r.call(e,t)},l=function(e){for(var t=i.call(e.getAttribute("class")||""),n=t?t.split(/\s+/):[],o=0,r=n.length;o<r;o++)this.push(n[o]);this._updateClassName=function(){e.setAttribute("class",this.toString())}},c=l.prototype=[],u=function(){return new l(this)};if(a.prototype=Error.prototype,c.item=function(e){return this[e]||null},c.contains=function(e){return-1!==s(this,e+="")},c.add=function(){var e,t=arguments,n=0,o=t.length,i=!1;do{e=t[n]+"",-1===s(this,e)&&(this.push(e),i=!0)}while(++n<o);i&&this._updateClassName()},c.remove=function(){var e,t,n=arguments,o=0,i=n.length,r=!1;do{for(e=n[o]+"",t=s(this,e);-1!==t;)this.splice(t,1),r=!0,t=s(this,e)}while(++o<i);r&&this._updateClassName()},c.toggle=function(e,t){e+="";var n=this.contains(e),o=n?!0!==t&&"remove":!1!==t&&"add";return o&&this[o](e),!0===t||!1===t?t:!n},c.toString=function(){return this.join(" ")},o.defineProperty){var d={get:u,enumerable:!0,configurable:!0};try{o.defineProperty(n,t,d)}catch(e){void 0!==e.number&&-2146823252!==e.number||(d.enumerable=!1,o.defineProperty(n,t,d))}}else o.prototype.__defineGetter__&&n.__defineGetter__(t,u)}}(window.self),function(){"use strict";var e=document.createElement("_");if(e.classList.add("c1","c2"),!e.classList.contains("c2")){var t=function(e){var t=DOMTokenList.prototype[e];DOMTokenList.prototype[e]=function(e){var n,o=arguments.length;for(n=0;n<o;n++)e=arguments[n],t.call(this,e)}};t("add"),t("remove")}if(e.classList.toggle("c3",!1),e.classList.contains("c3")){var n=DOMTokenList.prototype.toggle;DOMTokenList.prototype.toggle=function(e,t){return 1 in arguments&&!this.contains(e)==!t?t:n.call(this,e)}}e=null}())},{}],2:[function(e,t,n){t.exports=function(e,t){if("string"!=typeof e)throw new TypeError("String expected");t||(t=document);var n=/<([\w:]+)/.exec(e);if(!n)return t.createTextNode(e);e=e.replace(/^\s+|\s+$/g,"");var o=n[1];if("body"==o)return(i=t.createElement("html")).innerHTML=e,i.removeChild(i.lastChild);var i,a=r[o]||r._default,s=a[0],l=a[1],c=a[2];for((i=t.createElement("div")).innerHTML=l+e+c;s--;)i=i.lastChild;if(i.firstChild==i.lastChild)return i.removeChild(i.firstChild);for(var u=t.createDocumentFragment();i.firstChild;)u.appendChild(i.removeChild(i.firstChild));return u};var o,i=!1;"undefined"!=typeof document&&((o=document.createElement("div")).innerHTML='  <link/><table></table><a href="/a">a</a><input type="checkbox"/>',i=!o.getElementsByTagName("link").length,o=void 0);var r={legend:[1,"<fieldset>","</fieldset>"],tr:[2,"<table><tbody>","</tbody></table>"],col:[2,"<table><tbody></tbody><colgroup>","</colgroup></table>"],_default:i?[1,"X<div>","</div>"]:[0,"",""]};r.td=r.th=[3,"<table><tbody><tr>","</tr></tbody></table>"],r.option=r.optgroup=[1,'<select multiple="multiple">',"</select>"],r.thead=r.tbody=r.colgroup=r.caption=r.tfoot=[1,"<table>","</table>"],r.polyline=r.ellipse=r.polygon=r.circle=r.text=r.line=r.path=r.rect=r.g=[1,'<svg xmlns="http://www.w3.org/2000/svg" version="1.1">',"</svg>"]},{}],3:[function(e,t,n){"use strict";function o(e,t){if(null==e)throw new TypeError("Cannot convert first argument to object");for(var n=Object(e),o=1;o<arguments.length;o++){var i=arguments[o];if(null!=i)for(var r=Object.keys(Object(i)),a=0,s=r.length;a<s;a++){var l=r[a],c=Object.getOwnPropertyDescriptor(i,l);void 0!==c&&c.enumerable&&(n[l]=i[l])}}return n}t.exports={assign:o,polyfill:function(){Object.assign||Object.defineProperty(Object,"assign",{enumerable:!1,configurable:!0,writable:!0,value:o})}}},{}],4:[function(e,t,n){var o=/^(?:submit|button|image|reset|file)$/i,i=/^(?:input|select|textarea|keygen)/i,r=/(\[[^\[\]]*\])/g;function a(e,t,n){if(0===t.length)return n;var o=t.shift(),i=o.match(/^\[(.+?)\]$/);if("[]"===o)return e=e||[],Array.isArray(e)?e.push(a(null,t,n)):(e._values=e._values||[],e._values.push(a(null,t,n))),e;if(i){var r=i[1],s=+r;isNaN(s)?(e=e||{})[r]=a(e[r],t,n):(e=e||[])[s]=a(e[s],t,n)}else e[o]=a(e[o],t,n);return e}function s(e,t,n){if(t.match(r))a(e,function(e){var t=[],n=new RegExp(r),o=/^([^\[\]]*)/.exec(e);for(o[1]&&t.push(o[1]);null!==(o=n.exec(e));)t.push(o[1]);return t}(t),n);else{var o=e[t];o?(Array.isArray(o)||(e[t]=[o]),e[t].push(n)):e[t]=n}return e}function l(e,t,n){return n=n.replace(/(\r)?\n/g,"\r\n"),n=(n=encodeURIComponent(n)).replace(/%20/g,"+"),e+(e?"&":"")+encodeURIComponent(t)+"="+n}t.exports=function(e,t){"object"!=typeof t?t={hash:!!t}:void 0===t.hash&&(t.hash=!0);for(var n=t.hash?{}:"",r=t.serializer||(t.hash?s:l),a=e&&e.elements?e.elements:[],c=Object.create(null),u=0;u<a.length;++u){var d=a[u];if((t.disabled||!d.disabled)&&d.name&&i.test(d.nodeName)&&!o.test(d.type)){var f=d.name,p=d.value;if("checkbox"!==d.type&&"radio"!==d.type||d.checked||(p=void 0),t.empty){if("checkbox"!==d.type||d.checked||(p=""),"radio"===d.type&&(c[d.name]||d.checked?d.checked&&(c[d.name]=!0):c[d.name]=!1),!p&&"radio"==d.type)continue}else if(!p)continue;if("select-multiple"!==d.type)n=r(n,f,p);else{p=[];for(var h=d.options,v=!1,m=0;m<h.length;++m){var g=h[m],y=t.empty&&!g.value,b=g.value||y;g.selected&&b&&(v=!0,n=t.hash&&"[]"!==f.slice(f.length-2)?r(n,f+"[]",g.value):r(n,f,g.value))}!v&&t.empty&&(n=r(n,f,""))}}}if(t.empty)for(var f in c)c[f]||(n=r(n,f,""));return n}},{}],5:[function(e,t,n){(function(o){!function(e){"object"==typeof n&&void 0!==t?t.exports=e():("undefined"!=typeof window?window:void 0!==o?o:"undefined"!=typeof self?self:this).vexDialog=e()}((function(){return function t(n,o,i){function r(s,l){if(!o[s]){if(!n[s]){var c="function"==typeof e&&e;if(!l&&c)return c(s,!0);if(a)return a(s,!0);var u=new Error("Cannot find module '"+s+"'");throw u.code="MODULE_NOT_FOUND",u}var d=o[s]={exports:{}};n[s][0].call(d.exports,(function(e){return r(n[s][1][e]||e)}),d,d.exports,t,n,o,i)}return o[s].exports}for(var a="function"==typeof e&&e,s=0;s<i.length;s++)r(i[s]);return r}({1:[function(e,t,n){t.exports=function(e,t){if("string"!=typeof e)throw new TypeError("String expected");t||(t=document);var n=/<([\w:]+)/.exec(e);if(!n)return t.createTextNode(e);e=e.replace(/^\s+|\s+$/g,"");var o=n[1];if("body"==o)return(i=t.createElement("html")).innerHTML=e,i.removeChild(i.lastChild);var i,a=r[o]||r._default,s=a[0],l=a[1],c=a[2];for((i=t.createElement("div")).innerHTML=l+e+c;s--;)i=i.lastChild;if(i.firstChild==i.lastChild)return i.removeChild(i.firstChild);for(var u=t.createDocumentFragment();i.firstChild;)u.appendChild(i.removeChild(i.firstChild));return u};var o,i=!1;"undefined"!=typeof document&&((o=document.createElement("div")).innerHTML='  <link/><table></table><a href="/a">a</a><input type="checkbox"/>',i=!o.getElementsByTagName("link").length,o=void 0);var r={legend:[1,"<fieldset>","</fieldset>"],tr:[2,"<table><tbody>","</tbody></table>"],col:[2,"<table><tbody></tbody><colgroup>","</colgroup></table>"],_default:i?[1,"X<div>","</div>"]:[0,"",""]};r.td=r.th=[3,"<table><tbody><tr>","</tr></tbody></table>"],r.option=r.optgroup=[1,'<select multiple="multiple">',"</select>"],r.thead=r.tbody=r.colgroup=r.caption=r.tfoot=[1,"<table>","</table>"],r.polyline=r.ellipse=r.polygon=r.circle=r.text=r.line=r.path=r.rect=r.g=[1,'<svg xmlns="http://www.w3.org/2000/svg" version="1.1">',"</svg>"]},{}],2:[function(e,t,n){var o=/^(?:submit|button|image|reset|file)$/i,i=/^(?:input|select|textarea|keygen)/i,r=/(\[[^\[\]]*\])/g;function a(e,t,n){if(0===t.length)return n;var o=t.shift(),i=o.match(/^\[(.+?)\]$/);if("[]"===o)return e=e||[],Array.isArray(e)?e.push(a(null,t,n)):(e._values=e._values||[],e._values.push(a(null,t,n))),e;if(i){var r=i[1],s=+r;isNaN(s)?(e=e||{})[r]=a(e[r],t,n):(e=e||[])[s]=a(e[s],t,n)}else e[o]=a(e[o],t,n);return e}function s(e,t,n){if(t.match(r))a(e,function(e){var t=[],n=new RegExp(r),o=/^([^\[\]]*)/.exec(e);for(o[1]&&t.push(o[1]);null!==(o=n.exec(e));)t.push(o[1]);return t}(t),n);else{var o=e[t];o?(Array.isArray(o)||(e[t]=[o]),e[t].push(n)):e[t]=n}return e}function l(e,t,n){return n=n.replace(/(\r)?\n/g,"\r\n"),n=(n=encodeURIComponent(n)).replace(/%20/g,"+"),e+(e?"&":"")+encodeURIComponent(t)+"="+n}t.exports=function(e,t){"object"!=typeof t?t={hash:!!t}:void 0===t.hash&&(t.hash=!0);for(var n=t.hash?{}:"",r=t.serializer||(t.hash?s:l),a=e&&e.elements?e.elements:[],c=Object.create(null),u=0;u<a.length;++u){var d=a[u];if((t.disabled||!d.disabled)&&d.name&&i.test(d.nodeName)&&!o.test(d.type)){var f=d.name,p=d.value;if("checkbox"!==d.type&&"radio"!==d.type||d.checked||(p=void 0),t.empty){if("checkbox"!==d.type||d.checked||(p=""),"radio"===d.type&&(c[d.name]||d.checked?d.checked&&(c[d.name]=!0):c[d.name]=!1),!p&&"radio"==d.type)continue}else if(!p)continue;if("select-multiple"!==d.type)n=r(n,f,p);else{p=[];for(var h=d.options,v=!1,m=0;m<h.length;++m){var g=h[m],y=t.empty&&!g.value,b=g.value||y;g.selected&&b&&(v=!0,n=t.hash&&"[]"!==f.slice(f.length-2)?r(n,f+"[]",g.value):r(n,f,g.value))}!v&&t.empty&&(n=r(n,f,""))}}}if(t.empty)for(var f in c)c[f]||(n=r(n,f,""));return n}},{}],3:[function(e,t,n){var o=e("domify"),i=e("form-serialize"),r=function(e){var t=document.createElement("div");t.classList.add("vex-dialog-buttons");for(var n=0;n<e.length;n++){var o=e[n],i=document.createElement("button");i.type=o.type,i.textContent=o.text,i.className=o.className,i.classList.add("vex-dialog-button"),0===n?i.classList.add("vex-first"):n===e.length-1&&i.classList.add("vex-last"),function(e){i.addEventListener("click",function(t){e.click&&e.click.call(this,t)}.bind(this))}.bind(this)(o),t.appendChild(i)}return t};t.exports=function(e){var t={name:"dialog",open:function(t){var n=Object.assign({},this.defaultOptions,t);n.unsafeMessage&&!n.message?n.message=n.unsafeMessage:n.message&&(n.message=e._escapeHtml(n.message));var i=n.unsafeContent=function(e){var t=document.createElement("form");t.classList.add("vex-dialog-form");var n=document.createElement("div");n.classList.add("vex-dialog-message"),n.appendChild(e.message instanceof window.Node?e.message:o(e.message));var i=document.createElement("div");return i.classList.add("vex-dialog-input"),i.appendChild(e.input instanceof window.Node?e.input:o(e.input)),t.appendChild(n),t.appendChild(i),t}(n),a=e.open(n),s=n.beforeClose&&n.beforeClose.bind(a);if(a.options.beforeClose=function(){var e=!s||s();return e&&n.callback(this.value||!1),e}.bind(a),i.appendChild(r.call(a,n.buttons)),a.form=i,i.addEventListener("submit",n.onSubmit.bind(a)),n.focusFirstInput){var l=a.contentEl.querySelector("button, input, select, textarea");l&&l.focus()}return a},alert:function(e){return"string"==typeof e&&(e={message:e}),e=Object.assign({},this.defaultOptions,this.defaultAlertOptions,e),this.open(e)},confirm:function(e){if("object"!=typeof e||"function"!=typeof e.callback)throw new Error("dialog.confirm(options) requires options.callback.");return e=Object.assign({},this.defaultOptions,this.defaultConfirmOptions,e),this.open(e)},prompt:function(t){if("object"!=typeof t||"function"!=typeof t.callback)throw new Error("dialog.prompt(options) requires options.callback.");var n=Object.assign({},this.defaultOptions,this.defaultPromptOptions),o={unsafeMessage:'<label for="vex">'+e._escapeHtml(t.label||n.label)+"</label>",input:'<input name="vex" type="text" class="vex-dialog-prompt-input" placeholder="'+e._escapeHtml(t.placeholder||n.placeholder)+'" value="'+e._escapeHtml(t.value||n.value)+'" />'},i=(t=Object.assign(n,o,t)).callback;return t.callback=function(e){if("object"==typeof e){var t=Object.keys(e);e=t.length?e[t[0]]:""}i(e)},this.open(t)},buttons:{YES:{text:"OK",type:"submit",className:"vex-dialog-button-primary",click:function(){this.value=!0}},NO:{text:"Cancel",type:"button",className:"vex-dialog-button-secondary",click:function(){this.value=!1,this.close()}}}};return t.defaultOptions={callback:function(){},afterOpen:function(){},message:"",input:"",buttons:[t.buttons.YES,t.buttons.NO],showCloseButton:!1,onSubmit:function(e){return e.preventDefault(),this.options.input&&(this.value=i(this.form,{hash:!0})),this.close()},focusFirstInput:!0},t.defaultAlertOptions={buttons:[t.buttons.YES]},t.defaultPromptOptions={label:"Prompt:",placeholder:"",value:""},t.defaultConfirmOptions={},t}},{domify:1,"form-serialize":2}]},{},[3])(3)}))}).call(this,"undefined"!=typeof global?global:"undefined"!=typeof self?self:"undefined"!=typeof window?window:{})},{domify:2,"form-serialize":4}],6:[function(e,t,n){var o=e("./vex");o.registerPlugin(e("vex-dialog")),t.exports=o},{"./vex":7,"vex-dialog":5}],7:[function(e,t,n){e("classlist-polyfill"),e("es6-object-assign").polyfill();var o=e("domify"),i=function(e){if(void 0!==e){var t=document.createElement("div");return t.appendChild(document.createTextNode(e)),t.innerHTML}return""},r=function(e,t){if("string"==typeof t&&0!==t.length)for(var n=t.split(" "),o=0;o<n.length;o++){var i=n[o];i.length&&e.classList.add(i)}},a=function(){var e=document.createElement("div"),t={animation:"animationend",WebkitAnimation:"webkitAnimationEnd",MozAnimation:"animationend",OAnimation:"oanimationend",msAnimation:"MSAnimationEnd"};for(var n in t)if(void 0!==e.style[n])return t[n];return!1}(),s="vex-closing",l="vex-open",c={},u=1,d=!1,f={open:function(e){var t=function(e){console.warn('The "'+e+'" property is deprecated in vex 3. Use CSS classes and the appropriate "ClassName" options, instead.'),console.warn("See http://github.hubspot.com/vex/api/advanced/#options")};e.css&&t("css"),e.overlayCSS&&t("overlayCSS"),e.contentCSS&&t("contentCSS"),e.closeCSS&&t("closeCSS");var n={};n.id=u++,c[n.id]=n,n.isOpen=!0,n.close=function(){if(!this.isOpen)return!0;var e=this.options;if(d&&!e.escapeButtonCloses)return!1;if(!1===function(){return!e.beforeClose||e.beforeClose.call(this)}.bind(this)())return!1;this.isOpen=!1;var t=window.getComputedStyle(this.contentEl);function n(e){return"none"!==t.getPropertyValue(e+"animation-name")&&"0s"!==t.getPropertyValue(e+"animation-duration")}var o=n("")||n("-webkit-")||n("-moz-")||n("-o-"),i=function t(){this.rootEl.parentNode&&(this.rootEl.removeEventListener(a,t),this.overlayEl.removeEventListener(a,t),delete c[this.id],this.rootEl.parentNode.removeChild(this.rootEl),this.bodyEl.removeChild(this.overlayEl),e.afterClose&&e.afterClose.call(this),0===Object.keys(c).length&&document.body.classList.remove(l))}.bind(this);return a&&o?(this.rootEl.addEventListener(a,i),this.overlayEl.addEventListener(a,i),this.rootEl.classList.add(s),this.overlayEl.classList.add(s)):i(),!0},"string"==typeof e&&(e={content:e}),e.unsafeContent&&!e.content?e.content=e.unsafeContent:e.content&&(e.content=i(e.content));var p=n.options=Object.assign({},f.defaultOptions,e),h=n.bodyEl=document.getElementsByTagName("body")[0],v=n.rootEl=document.createElement("div");v.classList.add("vex"),r(v,p.className);var m=n.overlayEl=document.createElement("div");m.classList.add("vex-overlay"),r(m,p.overlayClassName),p.overlayClosesOnClick&&v.addEventListener("click",(function(e){e.target===v&&n.close()})),h.appendChild(m);var g=n.contentEl=document.createElement("div");if(g.classList.add("vex-content"),r(g,p.contentClassName),g.appendChild(p.content instanceof window.Node?p.content:o(p.content)),v.appendChild(g),p.showCloseButton){var y=n.closeEl=document.createElement("div");y.classList.add("vex-close"),r(y,p.closeClassName),y.addEventListener("click",n.close.bind(n)),g.appendChild(y)}return document.querySelector(p.appendLocation).appendChild(v),p.afterOpen&&p.afterOpen.call(n),document.body.classList.add(l),n},close:function(e){var t;if(e.id)t=e.id;else{if("string"!=typeof e)throw new TypeError("close requires a vex object or id string");t=e}return!!c[t]&&c[t].close()},closeTop:function(){var e=Object.keys(c);return!!e.length&&c[e[e.length-1]].close()},closeAll:function(){for(var e in c)this.close(e);return!0},getAll:function(){return c},getById:function(e){return c[e]}};window.addEventListener("keyup",(function(e){27===e.keyCode&&(d=!0,f.closeTop(),d=!1)})),window.addEventListener("popstate",(function(){f.defaultOptions.closeAllOnPopState&&f.closeAll()})),f.defaultOptions={content:"",showCloseButton:!0,escapeButtonCloses:!0,overlayClosesOnClick:!0,appendLocation:"body",className:"",overlayClassName:"",contentClassName:"",closeClassName:"",closeAllOnPopState:!0},Object.defineProperty(f,"_escapeHtml",{configurable:!1,enumerable:!1,writable:!1,value:i}),f.registerPlugin=function(e,t){var n=e(f),o=t||n.name;if(f[o])throw new Error("Plugin "+t+" is already registered.");f[o]=n},t.exports=f},{"classlist-polyfill":1,domify:2,"es6-object-assign":3}]},{},[6])(6)}));