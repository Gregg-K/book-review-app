function Dashboard() {
  const user = JSON.parse(localStorage.getItem("user"));

  function logout() {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    window.location.href = "/login";
  }

  if (!user) {
    return <h2>Please login first</h2>;
  }

  return (
    <div>
      <h2>Dashboard</h2>
      <p>Welcome, {user.username}</p>
      <p>Email: {user.email}</p>

      <button onClick={logout}>Logout</button>
    </div>
  );
}

export default Dashboard;