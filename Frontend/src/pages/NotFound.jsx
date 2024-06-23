import React from 'react'
import { Link } from 'react-router-dom'

function NotFound() {
  return (
    <>
    <div>404 not found</div>
    <div>The page you are looking for does not exist!</div>

    <Link to="/landingpage">
        <button>Go to Landing page</button>
      </Link>
    </>
  )
}

export default NotFound