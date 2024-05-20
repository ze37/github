import Banner from "./components/Banner";
import Container from "./components/Container";
import Footer from "./components/Footer";
import Header from "./components/Header";

function App() {
  return (
    <>
      <Header />
      <Banner />
      <Container>
        <h1>Ola mundo</h1>
      </Container>
      <Footer />
    </>
  );
}

export default App;
