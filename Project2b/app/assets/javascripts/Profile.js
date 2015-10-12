var total = parseInt(document.getElementById('bitbar_count').className);

function showBitbars(bitbars) 
{
    document.getElementById("bitbar_display").innerHTML = bitbars + " bitbars";
    if (bitbars < total) 
    {
    	setTimeout(function(){
    		showBitbars(bitbars+1);
    	}, 20);
    }
}
      
if (total > 0) 
{
	showBitbars(0);
}