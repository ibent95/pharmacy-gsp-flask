
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