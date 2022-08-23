export { }

declare global {
	interface Window {
		onDeleteData: any; // (data: any, url?: string) => void
		onDeleteDrug: any; // (data: any, url?: string) => void
		onDeleteTransaction: any; // (data: any, url?: string) => void
		onDeleteUser: any; // (data: any, url?: string) => void
	}
};

import Swal from 'sweetalert2';

window.document.addEventListener("DOMContentLoaded", function () {

	//Swal.fire('Hi from webpack!');

	//var vex = require('vex-js')
	//vex.registerPlugin(require('vex-dialog'))
	//vex.defaultOptions.className = 'vex-theme-os'

	//vex.dialog.alert('I was made by a plugin!');
	window.onDeleteData = function(data: any, url: string): void {
		if (window.confirm("Yakin ingin menghapus data ini?")) window.location.href = url;
	}

	/** Dashboard page`s functions */
	/** GSP page`s functions */
	/** Drug page`s functions */
	window.onDeleteDrug = function(data: any, url: string): void {
		if (window.confirm("Yakin ingin menghapus data obat " + data + "?")) window.location.href = url;
	}

	/** Transaction page`s functions */
	window.onDeleteTransaction = function(data: any, url: string): void {
		if (window.confirm("Yakin ingin menghapus data transaksi " + data + "?")) window.location.href = url;
	}

	/** User page`s functions */
	window.onDeleteUser = function(data: any, url: string): void {
		if (window.confirm("Yakin ingin menghapus data pengguna " + data + "?")) window.location.href = url;
	}

});