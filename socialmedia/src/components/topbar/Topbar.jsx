import "./topbar.css"
import {Search} from "@mui/icons-material"
export default function Topbar() {
  return (
    <div  className="topbarContainer">
        <div className="topbarLeft">
          <span className="logo">Lamasocial</span>
        </div>
        <div className="topbarCenter">
          <div className="searchbar">
            <Search/>
            <input placeholder="Search for friend, post or video" className="searchInput" />
          </div>
        </div>
        <div className="topbarRight"></div>
    </div>
  )
}
