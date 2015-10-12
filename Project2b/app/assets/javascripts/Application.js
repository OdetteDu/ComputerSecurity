// if(top.location != self.location)
// {
//     parent.location = self.location;
// }
if (self == top)
{
	document.documentElement.style.visibility = 'visible';
}
else
{
	top.location = self.location;
}