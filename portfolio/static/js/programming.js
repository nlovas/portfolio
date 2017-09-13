
function format(pData){
	//makes point form work & inline html
	var myPartsDiv;
	var tmp;
    for(i=0;i<pData.length;i++){

        myPartsDiv = document.createElement("div");
        myPartsDiv.className = "mypartsPP" + i;


        myPartsDiv.innerHTML = pData[i]["myParts"];
        //console.log(myPartsDiv);
        //tmp = ".languagesofPP" + i.toString() + "";
        //console.log(tmp);
        tmp = $(".languagesofPP" + i);
        $(tmp).after(myPartsDiv);
    }
    //$("mypartsofPP");
	//alert(pData[0]['title']);
	// var pData = [{"myParts": "laaaaaaaaaaaalalalalalallalalalaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}];
}