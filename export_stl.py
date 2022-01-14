# STL exporter

def exportStl(file_name, label, x, y, z, ox, oy, oz):
    name = file_name + ".stl"
    with open(name, mode='a') as stl_file:
        stl_file.write('solid ' + label + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')

        #		stl_file.write('    vertex 0.0 0.0 0.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex 0.0 0.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex 0.0 0.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 0.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex 0.0 0.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 0.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 0.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 0.0'+'\n')

        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('endsolid ' + label + '\n')
