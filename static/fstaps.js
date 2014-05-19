
function showEdit(barName, index){
	showOrHideGroups(barName, index, true);
}

function hideEdit(barName, index){
	showOrHideGroups(barName, index, false);
}

function showOrHideGroups(barName, index, show){
	for(i = 1; i < 4; i++){
		showOrHide($('#edit_' + barName + '_' + i), false);
		showOrHide($('#' + barName + i), !show);
	}
	showOrHide($('#floor_' + barName), !show);
	showOrHide($('#edit_' + barName + '_' + index), show);
}

function showOrHide(obj, show){
	if(show){
		obj.show();
	}	
	else{
		obj.hide();
	}
}
