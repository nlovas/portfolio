
function format(pData,pImages){
	//makes point form work, inline html, sets up images
	var myPartsDiv;
	var tmp;
	var tmp2;
    for(i=0;i<pData.length;i++){

        //for the bullets:
        myPartsDiv = document.createElement("div");
        myPartsDiv.className = "mypartsPP" + i;
        myPartsDiv.innerHTML = "My roles included:<br/>" + pData[i]["myParts"];
        //tmp = $(".languagesofPP" + i);
        $(".languagesofPP" + i).after(myPartsDiv);
        //for the description(so the links are formatted correctly, etc)
        descDiv  = document.createElement("div");
        descDiv.className = "descPP" + i;
        descDiv.innerHTML = "Description:<br/>" + pData[i]["desc"];
        //tmp2 = $(".sourcecodeofPP" + i);
        $(".sourcecodeofPP" + i).after(descDiv);

        //for the images
        for(p=0;p<pImages[i].length;p++){
            thumbnail = document.createElement("img");
            thumbnail.className = "PP" + i + "image" + p;
            thumbnail.className = "img-responsive";
            thumbnail.className = "smol-img";
            $(thumbnail).attr("alt","Screenshot of " + pData[i]["title"]);
            $(thumbnail).attr("src", "../static/images" + pImages[i][p]);

            $(".PP" + i).append(thumbnail);

        }

    }
    //$("mypartsofPP");
	//alert(pData[0]['title']);
	// var pData = [{"myParts": "laaaaaaaaaaaalalalalalallalalalaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}];
}

function prepareImages(pImages){
    //sets up the images on the page to behave properly


}