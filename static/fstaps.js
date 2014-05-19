
function showEdit(barName, index){
	for(i = 1; i < 4; i++){
		$('#edit_' + barName + '_' + i).hide();
		$('#' + barName + i).hide();
	}
	$('#floor_' + barName).hide();
	$('#edit_' + barName + '_' + index).show();
}

function hideEdit(barName, index){
	//TODO
}
