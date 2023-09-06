n, k, m = input().split(" ")


def production(n_in, k_in, m_in, parts_old):
    blanks = n_in // k_in
    parts_in = (k_in // m_in) * blanks
    residues = n_in - (m_in * parts_in)
    parts_old = parts_old + parts_in
    if residues >= k_in:
        production(residues, k_in, m_in, parts_old)
    elif residues == m_in and residues < 2 * m_in:
        parts_old += 1
        print(parts_old)
    else:
        print(parts_old)


production(int(n), int(k), int(m), 0)
