import "./topbar.css"
import {Search,Person,Chat,Notifications} from "@mui/icons-material"
export default function Topbar({ilgeesen}) {
  return (
    <>
    {JSON.stringify(ilgeesen)}
    <div  className="topbarContainer">
        <div className="topbarLeft">
          <span className="logo">{ilgeesen.data.username}</span>
        </div>
        <div className="topbarCenter">
          <div className="searchbar">
            <Search className="searchIcon"/>
            <input 
              placeholder="Search for friend, post or video" 
              className="searchInput"
            />
          </div>
        </div>
        <div className="topbarRight">
          <div className="topbarLinks">
            <span className="topbarLinks">Homepage</span>
            <span className="topbarLinks">Timeline</span>
          </div>
          <div className="topbarIcon">
            <div className="topbarIconItems">
              <Person/>
              <span className="topbarIconBadge">{ilgeesen.data.friendrequest}</span>
            </div>
            <div className="topbarIconItems">
              <Chat/>
              <span className="topbarIconBadge">{ilgeesen.data.sms}</span>
            </div>
            <div className="topbarIconItems">
              <Notifications/>
              <span className="topbarIconBadge">{ilgeesen.data.notif}</span>
            </div>
          </div>
          <img src={ilgeesen.data.profilephoto} alt="" className="topbarImg" />
        </div>
    </div>
    </>
  );
}
