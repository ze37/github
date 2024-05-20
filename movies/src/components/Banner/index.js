import "./banner.css"

function Banner ({image}){
  return(
    <div className="banner" style={{backgroundImage:`url('/img/banner-${image}.png')`}}
    ></div>
  )
}

export default Banner
