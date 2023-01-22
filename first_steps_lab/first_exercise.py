import png
import pyqrcode
from pyqrcode import QRCode

address = "https://scontent.fsof10-1.fna.fbcdn.net/v/t1.18169-9/10421565_682487418486170_2149859528258653694_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=174925&_nc_ohc=DAOpym18b98AX9mmxAW&tn=9hR7dLGfDPtbFR4I&_nc_ht=scontent.fsof10-1.fna&oh=00_AfCG42hV3-kwRak4RvjhvtAVtk3F0u_mxc9qc8qroc39NQ&oe=63C54154"
url = pyqrcode.create(address)
url.png("smilkov", scale=8)