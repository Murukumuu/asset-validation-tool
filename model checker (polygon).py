import bpy

# PolyCount
results = []
verts, edges, polys = 0, 0, 0

for obj in bpy.context.selected_objects:
    if obj and obj.type == 'MESH':
        dg = bpy.context.evaluated_depsgraph_get()
        eval_obj = obj.evaluated_get(dg)
        mesh = eval_obj.to_mesh()

        counts = {
            'Object': obj.name,
            'Vertices': len(mesh.vertices),
            'Edges': len(mesh.edges),
            'Polygons': len(mesh.polygons)
        }

        verts += len(mesh.vertices)
        edges += len(mesh.edges)
        polys += len(mesh.polygons)
        
        eval_obj.to_mesh_clear()
        results.append(counts)

if results:
    print('[Polycount Check]')
    for a in results:
        print(
            f"{a['Object']} | "
            f"Vertices:{a['Vertices']} "
            f"Edges:{a['Edges']} "
            f"Polygons:{a['Polygons']}"
        )
        
print(f'Total : {verts} Verts, {edges} Edges, {polys} Polys')
