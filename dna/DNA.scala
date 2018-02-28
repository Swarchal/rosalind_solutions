object DNA {

  def countNucleotides(s: String) {
    /* rosalind.info/dna
       count nucleotides in a DNA sequence */
    val nucleotides = List('A', 'C', 'G', 'T').distinct
    nucleotides.foreach(c => print(s.count(_ == c) + " "))
  }

}
