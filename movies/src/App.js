import Banner from "./components/Banner";
import Card from "./components/Cards";
import Container from "./components/Container";
import Footer from "./components/Footer";
import Header from "./components/Header";

function App() {
  return (
    <>
      <Header />
      <Banner image="favoritos" />
      <Container>
        <h2>Geografia</h2>
        <section className="cards">
          <Card />
          <Card />
          <Card />
          <Card />
          <Card />
        </section>

      </Container>
      <Footer />
    </>
  );
}

export default App;
