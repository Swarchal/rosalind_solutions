object DNA {

  def countNucleotides(seq: String) {
    /* rosalind.info/dna
       count nucleotides in a DNA sequence */
    "ACGT".foreach(nuc => print(seq.count(_ == nuc) + " "))
  }

}
