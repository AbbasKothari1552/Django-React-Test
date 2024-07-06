import React from 'react'
import './App.css'
import { BrowserRouter , Route , Routes , Navigate } from 'react-router-dom'
import ProtectedRoute from './components/ProtectedRoute'
import LandingPage from './pages/LandingPage'
import Register from './pages/Register'
import Activate from './pages/Activate'
import Home from './pages/Home'
import Login from './pages/Login'
import NotFound from './pages/NotFound'

function Logout() {
  localStorage.clear()
  return <Navigate to="/landingpage" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

function App() {
  return (
      <BrowserRouter>
        <Routes>
          <Route 
            path="/" 
            element={
              <ProtectedRoute>
                <Home />
              </ProtectedRoute>
            } 
          />
          <Route path="/landingpage" element={<LandingPage />} />
          <Route path="/register" element={<Register />} />
          <Route path="/activate/:uid/:token" element={<Activate />} />
          <Route path="/login" element={<Login />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </BrowserRouter>
  )
}

export default App
